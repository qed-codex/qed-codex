---
{
  "module": "src/ReciprocityTheory/ReductiveGroups/ArithmeticGeometry/FundamentalDomains/ModerateCoefficientPositivityHolds.lean",
  "declarations": [
    "ReciprocityTheory.ChartRestriction.G.FD.moderateCoefficientPositivity_holds"
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

## Nonnegative frequencies and decay of moderate automorphic sections

[Theorem AGR.0480](https://andrewodesky.com/rh/lean/ReciprocityTheory.ChartRestriction.G.FD.moderateCoefficientPositivity_holds/)

Fix the arithmetic frame data described below over a CM field $E$, with CM type $\Psi$, rank $r$, Hermitian form $h$, lattice $\Lambda$, group $\Gamma$, and frame domain $\mathcal D$. Let $\lambda=(\lambda_{\tau,i})\in(\mathbb Z^r)^\Psi$, and let $P$ be a holomorphic section on $\mathcal D$ with its specified triangular and $\Gamma$ transformation laws. Write $n_\lambda(x)$ for its metric factor, $\ell_1(x)$ for the first minimum, and $a_{\xi,\nu}(x)$ for its Fourier coefficient at a nonzero isotropic $\xi\in\Lambda$ and frequency $\nu\in\mathbb R^\Psi$.

Suppose $C,A\in\mathbb R$ and $$|P(x)|n_\lambda(x)\le C\ell_1(x)^{-A}\qquad(x\in\mathcal D).$$ If $a_{\xi,\nu}(x)\ne0$, then $\nu_\tau\ge0$ for every $\tau\in\Psi$. For every $0<\eta<1$ there is $C_\eta\in\mathbb R$ such that, for every such $\xi$, every $\nu$, and every $x\in\mathcal D$ satisfying $c_\tau q_{x,\tau}(\tau\xi)\le1$ for all $\tau$, $$|a_{\xi,\nu}(x)|n_\lambda(x)\le C_\eta\ell_1(x)^{-A}\exp\!\left(-4\pi(1-\eta)\sum_\tau\nu_\tau t_{\xi,\tau}(x)\right).$$
