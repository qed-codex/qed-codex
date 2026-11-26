---
{
  "module": "src/Development/AutomorphicArithmetic/AutomorphicVarieties/BuildingsResidueChars/FrobeniusDualityComplexConj.lean",
  "declarations": [
    "UpperTheory.frobeniusDuality_complexConj"
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

## Conjugate Frobenius spectra from a polarized pairing

[Theorem AGR.0792](https://andrewodesky.com/rh/lean/UpperTheory.frobeniusDuality_complexConj/)

Let $E$ be a CM number field with algebraic closure $\Omega$, $\ell$ prime, $\iota:\overline{\mathbb Q}_\ell\simeq\mathbb C$ a field isomorphism, and $n\ge0$. Let $$r:G_E\to\operatorname{GL}_n(\overline{\mathbb Q}_\ell),\qquad\theta:G_E\to\overline{\mathbb Q}_\ell^\times$$ be group homomorphisms. Let $c\in G_{E^+}$ be a complex-conjugation element, let $\varepsilon_\ell$ be the cyclotomic character, and suppose $P\in\operatorname{GL}_n(\overline{\mathbb Q}_\ell)$ satisfies $$r(g)^tP\,r(cgc^{-1})=\varepsilon_\ell(g)^{1-n}\theta(g)P\qquad(g\in G_E).$$ Let $w\nmid\ell$ and let $B,B'$ be multisets of nonzero complex numbers. Suppose $r$ is unramified at $w,cw$, and its inverse-arithmetic-Frobenius eigenvalue multisets, after applying $\iota$, are respectively $$(Nw)^{(n-1)/2}B,\qquad (N(cw))^{(n-1)/2}B'.$$ If $\theta$ is unramified at $w$ with inverse-Frobenius eigenvalue $z\in\mathbb C^\times$ under $\iota$, then $$\{b'^{-1}:b'\in B'\}=\{bz^{-1}:b\in B\}.$$
