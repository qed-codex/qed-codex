---
{
  "module": "src/Development/WeilBound/RepresentationTheoryGL/SiegelWeilProof/HolomorphicContinuation/AnalyticDeterminants/FderivEqZeroOfVanish.lean",
  "declarations": [
    "PositivityTheory.Rg.Sw.LVs.holInt"
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

## Differentiation of holomorphic integrals over a compact space

[Theorem AG.0475](https://andrewodesky.com/rh/lean/PositivityTheory.Rg.Sw.LVs.holInt/)

Let $n\ge0$, let $V=M_{2n}(\mathbb C)$, and let $\Omega\subseteq V$ be open. Let $K$ be a compact topological space with a Borel measurable structure and finite measure $\mu$. Let $F:K\times V\to\mathbb C$ satisfy: each $F(k,\cdot)$ is $C^\infty$ over $\mathbb C$ on $\Omega$, and for every $N\ge0$ its $N$th complex Fréchet derivative is jointly continuous on $K\times\Omega$.

Then $G(x)=\int_KF(k,x)\,d\mu(k)$ is $C^\infty$ over $\mathbb C$ on $\Omega$, and for every $x\in\Omega$ and $v_1,\ldots,v_N\in V$, $$D^NG(x)[v_1,\ldots,v_N]=\int_KD_x^NF(k,x)[v_1,\ldots,v_N]\,d\mu(k).$$
