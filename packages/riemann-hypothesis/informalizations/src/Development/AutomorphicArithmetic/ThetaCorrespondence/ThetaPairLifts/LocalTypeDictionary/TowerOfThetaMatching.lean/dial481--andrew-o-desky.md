---
{
  "module": "src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/TowerOfThetaMatching.lean",
  "declarations": [
    "GlobalTheory.SqTower.tower_alt_bis"
  ],
  "author": "dial481",
  "writer": "Andrew O'Desky",
  "origin": "other-author",
  "source": "https://andrewodesky.com/rh/",
  "source_commit": "40e56bab026552e089d7afcfeff08d2defb9c005",
  "license": "with-permission"
}
---

As published on 26 November 2026.

## Tower identity: the twisted-to-untwisted ratio of square constants equals a ratio of Hecke L-values times the ratio of the constants of the definite triangle, up to explicit algebraic factors

[Theorem THETA.1.0028](https://andrewodesky.com/rh/lean/GlobalTheory.SqTower.tower_alt_bis/)

Assume the following four hypotheses.

(H1) ([Hypothesis list B: fifty-three assumed statements on Weil representations, theta lifts, discrete series, L-functions and complex multiplication](https://andrewodesky.com/rh/lean/GlobalTheory.FunPr.ThetaLocalInputs/)).

(H2) ([Theta integrals agree: for a matching datum the two theta integrals are proportional on matching functions, with a unique nonzero constant, and the constant changes by an L-value when a hyperbolic plane is removed](https://andrewodesky.com/rh/lean/GlobalTheory.IndefiniteRowSideFullHecke.WeilTensorModels.ThetaIntegralsAgree/)).

(H3) ([Local matching: a matching datum for two Hermitian spaces of complementary dimensions admits matched quotient maps](https://andrewodesky.com/rh/lean/GlobalTheory.IndefiniteRowSideFullHecke.WeilTensorModels.LocalMatching/)).

(H4) (*Non-vanishing of $L$-values.*) For all large parameters, in the sense of ([Grids of Hermitian spaces with Weil data, and properties of all grids with large parameters](https://andrewodesky.com/rh/lean/GlobalTheory.ChiGrid.GridData/)), every grid, with its family of characters $(\xi_t)_{t\in\mathcal T}$ and its base index $\mu_0$, has the following property. For all $0\le i,j<m$:

(a) for every $t\in\mathcal T$, the character $\nu_{t,i,j}$ has a partial $L$-function $\Lambda$, and $\Lambda(s)\ne0$ for every integer $s$ with $1-\gamma-(\kappa_j-\kappa_{j+1})\le s\le\rho(i,j)+\gamma$;

(b) each of the three characters $\nu_{\mu_0,i,j}$, $\nu_{\mu_0,i,j}\,\delta$, $\nu_{\mu_0,i,j}\,\delta'$ has a partial $L$-function $\Lambda$, and $\Lambda(s)\ne0$ for every integer $s\ge1$.

Then, for all large parameters, every grid, with its family of characters $(\xi_t)_{t\in\mathcal T}$ and its base index $\mu_0$, has the following property. Let Weil data on the grid be given, with their standard additive character $\psi$; let $\mathcal S$ be a choice of bases and normalisations for them and $\varrho$ archimedean matching data, and assume the rationality hypothesis for $(\mathcal S,\mu_0)$, in the sense of ([Rationality hypothesis for a grid with Weil data](https://andrewodesky.com/rh/lean/GlobalTheory.RowTest.NumbersIn/)). Square constants are taken for the adelic bases of $\mathcal S$ and for $\varrho$, in the sense of ([Square constants of a grid: matched test data and normalised measures](https://andrewodesky.com/rh/lean/GlobalTheory.FunObj.IsSquareConst/)). Let $0\le i,j<m$ and $t\in\mathcal T$, and suppose that

- the square $(i,j)$ is non-degenerate at $t$ and $c$ is a square constant at $(t,i,j)$;
- the square $(i,j)$ is non-degenerate at $\mu_0$ and $c_0$ is a square constant at $(\mu_0,i,j)$;
- $c^0\colon\mathcal T\to\mathbb C$ is a constant of a definite triangle of the square $(i,j)$, in the sense of ([Triangles of Hermitian spaces, their constants, and the definite triangle of a square](https://andrewodesky.com/rh/lean/GlobalTheory.IndefiniteRowSideFullHecke.UnitCharTriangle.Tri/));
- $\Lambda$ is the partial $L$-function of $\nu_{t,i,j}$ and $\Lambda_0$ is the partial $L$-function of $\nu_{\mu_0,i,j}$.

Then there are step ratios $u_1,\dots,u_{m-j-1}$ for $t$ and a unit $\zeta$ of $K$ away from $N_t$ such that $$\frac{c}{c_0}\;\prod_{l=1}^{\kappa_j}\frac{\Lambda(\gamma+l)}{\Lambda_0(\gamma+l)} \;=\;\jmath(\zeta)\;\prod_{l=1}^{m-j-1}u_l\;\cdot\;\frac{c^0(t)}{c^0(\mu_0)}\;\prod_{l=0}^{\kappa_{j+1}-1}\frac{\Lambda(\gamma+\kappa_j-l)}{\Lambda_0(\gamma+\kappa_j-l)} .$$ Here $\gamma=(t_0+r+6)/2$, and a quotient whose denominator is $0$ is read as $0$.
