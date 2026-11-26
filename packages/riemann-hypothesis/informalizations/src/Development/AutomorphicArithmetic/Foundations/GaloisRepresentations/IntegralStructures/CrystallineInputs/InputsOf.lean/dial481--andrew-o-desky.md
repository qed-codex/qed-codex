---
{
  "module": "src/Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/IntegralStructures/CrystallineInputs/InputsOf.lean",
  "declarations": [
    "UpperTheory.Gal.Int.Inp.ac"
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

## Cuspidal base change in prime degree without norm-character self-twists

[Theorem AGR.1629](https://andrewodesky.com/rh/lean/UpperTheory.Gal.Int.Inp.ac/)

Let $M/K$ be a Galois extension of totally complex number fields of prime degree $d$, and let $a\ge1$. Let $\pi$ be a cuspidal automorphic subrepresentation of $\operatorname{GL}_a(\mathbb A_K)$. Write $q_v$ for the residue cardinality at a finite place. Consider every nontrivial Hecke character $\eta$ of $K$ satisfying $\eta^d=1$ and, at all but finitely many places $w$ of $M$, $$q_w=q_v^f\quad\Longrightarrow\quad\eta_v(\varpi_v)^f=1\qquad(v=w|_K;\ f\in\mathbb N).$$ Assume no such $\eta$ satisfies the following condition: at almost every $v$ it is unramified and $\pi$ has a Satake multiset $B_v$ with $\eta_v(\varpi_v)B_v=B_v$.

Then there is a cuspidal automorphic subrepresentation $\Pi$ over $M$ with these three compatibilities: every Satake multiset $B_v$ for $\pi$ gives $\{\alpha^f:\alpha\in B_v\}$ for $\Pi$ at every $w|v$ with $q_w=q_v^f$; the infinitesimal character at $\tau:M\hookrightarrow\mathbb C$ equals that of $\pi$ at $\tau|_K$; and whenever a continuous field isomorphism $K_v\simeq M_w$ respects the inclusions of $K$, the corresponding local components of $\pi$ and $\Pi$ are intertwined by a complex-linear isomorphism under that field isomorphism.
