---
{
  "module": "src/Development/AutomorphicArithmetic/Foundations/Convolution/TraceSplitting/CoreDesc.lean",
  "declarations": [
    "UpperTheory.ConvolutionTheory.T.coreDesc"
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

## Cuspidal descent with a prescribed split local component

[Theorem AGR.0071](https://andrewodesky.com/rh/lean/UpperTheory.ConvolutionTheory.T.coreDesc/)

Assume the source's two trace-comparison and matching-test-function packages, described in the conventions. Let $E/F$ be a Galois extension of totally complex number fields of prime degree, and choose a generator $\sigma$ of its Galois group. Let $n\ge1$. Choose Haar measures on the norm-one adelic general linear groups over $E$ and $F$, and let $\Theta$ be a unitary twist operator implementing $\sigma$ on the cuspidal $L^2$ space over $E$. Let $V$ be an irreducible cuspidal summand with $\Theta V=V$. Suppose $V$ has prescribed infinitesimal-character multisets $\Lambda_\tau$ and unramified Satake multisets $t_w$ outside a finite set. Impose the following spectral exclusion condition: for every finite set of places of $F$, these parameters, away from the places above that set, are neither a sum of at least two positive-rank cuspidal parameter systems over $E$ with arbitrary complex norm twists, nor the cyclic base change of such a sum over $F$. Let $v$ be a finite place of $F$ and assume $F_v\to E_{w_0}$ is surjective for every $w_0\mid v$. Choose $w\mid v$ and a smooth irreducible local component $\tau'$ of $V$ at $w$. There is an irreducible cuspidal summand $V_0$ over $F$, with parameter systems $\Lambda_0,t_0$, such that $$\Lambda=\operatorname{BC}_\infty(\Lambda_0),\qquad t_w=\operatorname{BC}(t_0)_w\quad\text{at all but finitely many }w.$$ There is a local component $\tau$ of $V_0$ at $v$ and a complex linear isomorphism $T$ intertwining $\tau$ with $\tau'$ after the natural completion map $F_v\to E_w$. At infinity, base change restricts embeddings; at unramified places it raises Satake parameters to the residue-degree power.
