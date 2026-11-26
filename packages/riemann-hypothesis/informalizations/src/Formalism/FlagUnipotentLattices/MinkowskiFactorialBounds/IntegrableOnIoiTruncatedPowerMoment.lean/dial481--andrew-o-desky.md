---
{
  "module": "src/Formalism/FlagUnipotentLattices/MinkowskiFactorialBounds/IntegrableOnIoiTruncatedPowerMoment.lean",
  "declarations": [
    "Formalism.HermitianLatticeCounting.P.sup_bound_of_truncated_integral"
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

## A supremum bound from a truncated Fourier bound

[Theorem ANT.1011](https://andrewodesky.com/rh/lean/Formalism.HermitianLatticeCounting.P.sup_bound_of_truncated_integral/)

Let $\phi:\mathbb C\to\mathbb C$ be continuous and integrable for planar Lebesgue measure. Let $x>0$ and $M\in\mathbb R$. Set $c_x(0)=1$ and $c_x(t)=\min(1,(x/t)^3)$ for $t>0$. If $$\left|\int_{\mathbb C}e^{2i\operatorname{Im}(sz)}\phi(z)\,dz\right|\le M c_x(|s|)\qquad(s\in\mathbb C),$$ then $$|\phi(z)|\le\frac3\pi x^2M\qquad(z\in\mathbb C).$$
