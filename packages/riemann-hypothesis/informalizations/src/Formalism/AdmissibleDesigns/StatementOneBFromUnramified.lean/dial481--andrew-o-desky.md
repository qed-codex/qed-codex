---
{
  "module": "src/Formalism/AdmissibleDesigns/StatementOneBFromUnramified.lean",
  "declarations": [
    "Formalism.MainNotions.N.K.Closed.wildTriv_holds"
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

## Wild inertia acts trivially in an open-kernel prime-power quotient

[Theorem GC.0710](https://andrewodesky.com/rh/lean/Formalism.MainNotions.N.K.Closed.wildTriv_holds/)

Let $E$ be a number field, $\Omega/E$ an algebraic closure, $l$ a prime, and $\mathfrak p$ a finite place of $E$ not above $l$. Let $A\subset\Omega$ be a valuation subring above $\mathfrak p$, with valuation $v_A$. Let $M$ be any group and $\phi:\operatorname{Gal}(\Omega/E)\to M$ a homomorphism with open kernel such that every $\phi(g)$ has order dividing $l^n$ for some $n\ge0$ depending on $g$. If $\sigma\in\operatorname{Gal}(\Omega/E)$ satisfies $$v_A(\sigma(y)/y-1)<1\qquad(y\in\Omega^\times),$$ then $\phi(\sigma)=1$.
