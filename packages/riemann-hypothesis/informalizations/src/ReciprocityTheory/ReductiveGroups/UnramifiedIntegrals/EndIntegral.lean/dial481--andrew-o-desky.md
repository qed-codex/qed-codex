---
{
  "module": "src/ReciprocityTheory/ReductiveGroups/UnramifiedIntegrals/EndIntegral.lean",
  "declarations": [
    "ReciprocityTheory.ChartRestriction.L1.end_integral"
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

## Integrality of the formal CM multiplier at an inert prime

[Theorem PHT.0563](https://andrewodesky.com/rh/lean/ReciprocityTheory.ChartRestriction.L1.end_integral/)

Use the notation of ([Weierstrass series and good CM models](https://andrewodesky.com/rh/lean/Formalism.L2.Th1.CM.cW/)). Let $d$ be a nonnegative integer with $d\equiv3\pmod4$, and let $\Lambda\subset\mathbb C$ be a rank-two period lattice stable under $\omega_d$. Let $\ell\ge5$ be prime with $\ell\nmid d$, and suppose $X^2=-d$ has no solution modulo $\ell$. Choose a field isomorphism $\iota:\mathbb C\simeq\mathbb C_\ell$ and a good model $g_2,g_3$ of $(\Lambda,\iota)$ at $\ell$. Every coefficient of $$U\bigl(\iota(\omega_d)\log_U(T)\bigr)$$ has $\ell$-adic absolute value at most one.
