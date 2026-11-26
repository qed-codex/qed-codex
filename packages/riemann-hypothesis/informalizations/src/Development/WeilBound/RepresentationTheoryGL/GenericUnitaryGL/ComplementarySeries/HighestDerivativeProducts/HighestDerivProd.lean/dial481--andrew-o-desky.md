---
{
  "module": "src/Development/WeilBound/RepresentationTheoryGL/GenericUnitaryGL/ComplementarySeries/HighestDerivativeProducts/HighestDerivProd.lean",
  "declarations": [
    "GlobalTheory.RgGu.Leib.Hand.leibnizOrd"
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

## A filtration for derivatives of parabolic induction

[Theorem REP.0044](https://andrewodesky.com/rh/lean/GlobalTheory.RgGu.Leib.Hand.leibnizOrd/)

Let $k$ be a nonarchimedean local field, and let $\psi:k\to S^1$ be a continuous nontrivial additive character. Write $\pi_1\times\pi_2$ for normalized parabolic induction and $\pi^{(j)}$ for the unnormalized Bernstein–Zelevinsky derivative defined using $\psi$: restrict to the mirabolic subgroup, apply the nontrivial twisted-coinvariant functor $j-1$ times and then the trivial-coinvariant functor for $j\ge1$; put $\pi^{(0)}=\pi$. Let $r,t,\ell,n\ge0$ satisfy $r+t=n+\ell$, and let $\pi_1,\pi_2$ be smooth complex representations of $\mathrm{GL}_r(k),\mathrm{GL}_t(k)$.

The $\ell$th derivative of $\pi_1\times\pi_2$ has a decreasing filtration by subrepresentations $$F_0=(\pi_1\times\pi_2)^{(\ell)},\qquad F_{\ell+1}=0,$$ whose successive quotients, for $0\le i\le\ell$, are $$F_i/F_{i+1}\simeq\bigl(\pi_1^{(i)}\otimes|\det|^{(\ell-i)/2}\bigr)\times\bigl(\pi_2^{(\ell-i)}\otimes|\det|^{i/2}\bigr)$$ when $i\le r$ and $\ell-i\le t$. For the other indices, $F_i=F_{i+1}$.
