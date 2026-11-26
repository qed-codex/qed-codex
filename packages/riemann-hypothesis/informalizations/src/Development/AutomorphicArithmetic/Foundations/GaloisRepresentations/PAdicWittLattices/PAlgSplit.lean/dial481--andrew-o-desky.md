---
{
  "module": "src/Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/PAdicWittLattices/PAlgSplit.lean",
  "declarations": [
    "UpperTheory.Gal.G3.pAlgSplit"
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

## Splitting an etale algebra by its geometric points

[Theorem ALG.1170](https://andrewodesky.com/rh/lean/UpperTheory.Gal.G3.pAlgSplit/)

Assume the following geometric-point criterion: for every etale algebra $E/D$, if each homomorphism $D\to\Omega$ to an algebraically closed field has a unique extension $E\to\Omega$, then $D\to E$ is bijective. Let $A,A',C$ be commutative rings, with $A$-algebra structures on $A'$ and $C$, and assume $A'/A$ is etale. Let $J$ be a finite set and $\tau_j:A'\to C$ be $A$-algebra homomorphisms. Suppose that for every algebraically closed field $\Omega$ and ring homomorphisms $x:C\to\Omega$, $y:A'\to\Omega$ agreeing on $A$, there is a unique $j\in J$ such that $x\circ\tau_j=y$. Then there is a $C$-algebra isomorphism $$\Phi:C\otimes_A A'\simeq\prod_{j\in J}C,\qquad \Phi(1\otimes b)_j=\tau_j(b).$$
