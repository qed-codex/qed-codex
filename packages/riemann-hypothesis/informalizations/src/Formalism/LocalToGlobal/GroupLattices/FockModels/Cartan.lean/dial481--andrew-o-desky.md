---
{
  "module": "src/Formalism/LocalToGlobal/GroupLattices/FockModels/Cartan.lean",
  "declarations": [
    "Formalism.L2.G.Model.cartanOnto_proved"
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

## Surjectivity of multiplication of integral highest-weight polynomial lattices

[Theorem REP.0209](https://andrewodesky.com/rh/lean/Formalism.L2.G.Model.cartanOnto_proved/)

Let $O$ be a discrete valuation domain with fraction field $K$, let $N=m+1$ with $m\ge0$, and let $\Lambda\subset K^N$ be the $O$-span of the columns of some invertible matrix. Let $\lambda,\mu\in\mathbb Z^N$ be weakly decreasing. For a weakly decreasing row $\eta\in\mathbb Z^N$, put $H_\eta(\Lambda)=\mathscr H^\nabla_\eta(\Lambda)$, using the coefficient-lattice construction in ([Local polynomial lattice settings](https://andrewodesky.com/rh/lean/Formalism.MainNotions.G.GAtP/)) with $d_0=N$. Then $$H_{\lambda+\mu}(\Lambda)=\operatorname{span}_O\{FG:F\in H_\lambda(\Lambda),\ G\in H_\mu(\Lambda)\}.$$
