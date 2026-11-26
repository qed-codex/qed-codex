---
{
  "module": "src/Development/WeilBound/CoreStatements/AutomorphicKernels/GrothendieckRingPolynomial/TriSupportedLe.lean",
  "declarations": [
    "PositivityTheory.Groth.uniTri"
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

## A bounded triangular family is an integral basis

[Theorem ALG.1522](https://andrewodesky.com/rh/lean/PositivityTheory.Groth.uniTri/)

Let $M,I,C$ be sets, $L:M\simeq I$ a bijection, and let $c:M\to C$, $w:M\to\mathbb Z_{\ge0}$, $b:C\to\mathbb Z_{\ge0}$. Suppose $w(m)\le b(c(m))$. For each $m\in M$ take a finitely supported vector $f_m\in\mathbb Z^{(I)}$ satisfying $$f_m(L(m))=1,$$ $$f_m(L(n))\ne0\ \Longrightarrow\ c(m)=c(n)\text{ and }\bigl(m=n\text{ or }w(m)<w(n)\bigr).$$ Then the map $$\mathbb Z^{(M)}\longrightarrow\mathbb Z^{(I)},\qquad (a_m)\longmapsto\sum_m a_m f_m$$ is bijective. For each $n\in M$, the standard basis vector at $L(n)$ is a finite integer combination of the $f_m$ with $c(m)=c(n)$.
