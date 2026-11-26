---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/PchernOfStatement.lean",
  "declarations": [
    "GlobalTheory.T.pChern_neg_one"
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

## The Chern pairing of period classes

[Theorem AV.1441](https://andrewodesky.com/rh/lean/GlobalTheory.T.pChern_neg_one/)

Let $A$ be an abelian scheme over $\mathbb C$, and let $u:\mathbb C^g\to A(\mathbb C)$ be a holomorphic uniformization with lattice $\Lambda$, in the line-bundle uniformization model in the conventions. Let $P:\Lambda\to H^1_{\mathrm{dR}}(A/\mathbb C)^\vee$ be a period homomorphism, meaning that its values on primitive de Rham classes give their periods along lattice elements. Let $M$ be a line bundle on $A$, and let $u'$ be a line bundle uniformization for $M$ with the same exponential map as $u$. Suppose $u'$ has Appell–Humbert data $(H,\chi)$, with $H\in M_g(\mathbb C)$ and $\chi$ the associated multiplier on its lattice. Let $\Psi$ be a complex bilinear form on the de Rham period space representing the polarization form of $M$: there are finite families of primitive degree-one classes $a_j,b_j$ with $c_1(M)=\sum_j a_j\smile b_j$ and $\Psi(X,Y)=\sum_j(X(a_j)Y(b_j)-X(b_j)Y(a_j))$. Then for all $x,x'\in\Lambda$, $$\Psi(Px,Px')=-2\pi i\,\Im\bigl(x^tH\overline{x'}\bigr).$$
