import numpy as np
import matplotlib.pyplot as plt

# ==========================================
# Simulation Monte Carlo d'un Autocall
# ==========================================

# Paramètres de marché
S0 = 100               # Prix initial du sous-jacent
r = 0.02               # Taux sans risque
sigma = 0.25           # Volatilité du sous-jacent
T = 5                  # Maturité du produit (en années)
steps_per_year = 252   # Nombre de jours de trading par an
n_simulations = 10000  # Nombre de simulations Monte Carlo

# Paramètres du produit structuré
nominal = 100
coupon = 0.08
autocall_barrier = 100  # Niveau de barrière : si le sous-jacent ≥ 100 à une date d'observation → remboursement anticipé

# Pas de temps de la simulation
total_steps = T * steps_per_year
dt = T / total_steps

# Liste pour stocker les payoffs simulés
payoffs = []

# ==========================================
# Simulation Monte Carlo
# ==========================================
for _ in range(n_simulations):
    S = S0
    called = False

    for t in range(1, total_steps + 1):

        # Génération d'un choc aléatoire (mouvement brownien)
        z = np.random.normal(0, 1)

        # Évolution du prix du sous-jacent selon le modèle de Black-Scholes
        S = S * np.exp((r - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * z)

        # Dates d'observation annuelles pour vérifier l'autocall
        if t % steps_per_year == 0:

            observation_year = t / steps_per_year

            # Si le sous-jacent dépasse la barrière → remboursement anticipé
            if S >= autocall_barrier:

                payoff = nominal * (1 + coupon * observation_year)
                payoffs.append(payoff)
                called = True
                break

    # Si le produit n'est jamais autocallé → remboursement du nominal à maturité
    if not called:
        payoffs.append(nominal)

# Actualisation du payoff moyen pour obtenir le prix du produit
autocall_price = np.exp(-r * T) * np.mean(payoffs)

print(f"Prix estimé de l'autocall : {autocall_price:.2f}")

# ==========================================
# Visualisation de trajectoires simulées
# ==========================================

plt.figure(figsize=(10, 6))

# Simulation de quelques trajectoires pour visualisation
for _ in range(50):

    S = S0
    path = [S]

    for _ in range(total_steps):

        z = np.random.normal(0, 1)
        S = S * np.exp((r - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * z)
        path.append(S)

    plt.plot(path, linewidth=0.8)

plt.title("Trajectoires simulées du sous-jacent")
plt.xlabel("Pas de temps")
plt.ylabel("Prix du sous-jacent")
plt.grid(True)

plt.show()

