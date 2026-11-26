---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/TwistedOperators/EqZeroOfContr.lean",
  "declarations": [
    "GlobalTheory.Chain.IoLift.TensorFormProof.tensorForm"
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

## Representing finite-support sesquilinear forms by tensors

[Theorem ALG.1271](https://andrewodesky.com/rh/lean/GlobalTheory.Chain.IoLift.TensorFormProof.tensorForm/)

Let $U,A,V$ be complex vector spaces, $H$ a complex inner-product space, and $\iota:V\to H$ an injective linear map. For $y\in V$, define $$C_y:A\otimes_{\mathbb C}V\to A,\qquad C_y(a\otimes v)=\langle\iota y,\iota v\rangle a,$$ with inner product linear in the second argument. If $C_y(t)=0$ for every $y\in V$, then $t=0$.

Let $B:U\times V\to A$ be linear in the first argument and conjugate-linear in the second. Suppose that for each $P\in U$ there is a finite-dimensional subspace $E_P\subseteq V$ such that $B(P,y)=0$ whenever $\iota y$ is orthogonal to $\iota E_P$. There is a linear map $f:U\to A\otimes_{\mathbb C}V$ with $$C_y(f(P))=B(P,y)\qquad(P\in U,\ y\in V).$$
