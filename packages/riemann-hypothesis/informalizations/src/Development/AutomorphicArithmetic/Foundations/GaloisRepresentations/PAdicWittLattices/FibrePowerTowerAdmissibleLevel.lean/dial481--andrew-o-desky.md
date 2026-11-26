---
{
  "module": "src/Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/PAdicWittLattices/FibrePowerTowerAdmissibleLevel.lean",
  "declarations": [
    "UpperTheory.Gal.G3.genSm_holds",
    "UpperTheory.Gal.G3.polUniq_holds",
    "UpperTheory.Gal.G3.witForget_holds"
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

## Uniqueness of line bundles after an étale isogeny

[Theorem AV.1303](https://andrewodesky.com/rh/lean/UpperTheory.Gal.G3.polUniq_holds/)

Let $S$ be a scheme, let $A,A'$ be abelian schemes over $S$, and let $\psi:A\to A'$ be a finite, étale, surjective homomorphism. Let $P,Q$ be line bundles on $A'\times_S A'$. Assume that each of $P$ and $Q$ restricts to a trivial line bundle on both $\{0\}\times_S A'$ and $A'\times_S\{0\}$. If $$(\psi\times\psi)^*P\simeq(\psi\times\psi)^*Q,$$ then $P\simeq Q$.

## Smoothness and projectivity of generic PEL models

[Theorem AV.1440](https://andrewodesky.com/rh/lean/UpperTheory.Gal.G3.genSm_holds/)

Let $p$ be a rational prime and fix a full integral unitary PEL datum over a CM field $F$ in the source's model. Write $a,m,n$ for its signature and algebra-size parameters and $\mathcal B$ for its order. Let $R$ be a field equipped with a $\mathbb Q$-algebra structure and with compatible PEL base data. Let $N\ge3$ be coprime to $p$. Suppose $X\to\operatorname{Spec}R$ represents the corresponding PEL moduli problem at full level $N$, with its universal object and its universal property. Then this morphism is smooth, separated, and quasi-compact. It is projective if $$2a<[F:\mathbb Q]\qquad\text{or}\qquad(\mathcal B\otimes_{\mathbb Z}\mathbb Q\text{ is a division algebra and }n<2m).$$

## Finite etale maps forgetting prime-to-p level structure

[Theorem AV.1466](https://andrewodesky.com/rh/lean/UpperTheory.Gal.G3.witForget_holds/)

Let $p$ be prime and fix the source's full compatible PEL moduli datum, its adelic group and their comparison data. Let $R$ be a field with a $\mathbb Q$-algebra structure and a permitted base datum over $R$. Let $N,M\ge3$ be prime to $p$, with $N\mid M$, and let $X_N,X_M$ be arbitrary generic moduli models of these data at levels $N,M$, with universal abelian schemes $A_N,A_M$. There exist morphisms $$\pi:X_M\to X_N,\qquad\Phi:A_M\to A_N$$ such that $\pi$ is finite, etale and surjective, and $(\pi,\Phi)$ is a correspondence for the identity adelic element with the structure-preserving conditions in the conventions below.
