---
{
  "module": "src/Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/TranscendenceTraces/IsolateSpecHolds.lean",
  "declarations": [
    "UpperTheory.Gal.TranscendenceTraces.corrEqQ_holds",
    "UpperTheory.Gal.TranscendenceTraces.galTrans_holds",
    "UpperTheory.Gal.TranscendenceTraces.trDegQ_holds"
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

## A relation of finite correspondences detected on a dense set

[Theorem AG.0277](https://andrewodesky.com/rh/lean/UpperTheory.Gal.TranscendenceTraces.corrEqQ_holds/)

Assume that, for every ring map $R\to R'$, every sheaf of $R'$-modules and every integer degree, restriction of scalars induces a bijection on cohomology at every object where it is evaluated. Let $\ell$ be prime and $S\to B$, $Y\to B$ morphisms of schemes, with $Y\to B$ separated and locally of finite type. Assume that $\ell$ is invertible in $\Gamma(S,\mathcal O_S)$. Let $C_a=(Z_a,p_a,f_a,w_a)$ be finitely many weighted finite correspondences from $S$ to $Y$ over $B$, and let $m_a\in\mathbb Z$. Let $D\subseteq S$ be Zariski dense. Suppose for every algebraically closed $\Omega$, $x:\operatorname{Spec}\Omega\to S$ whose image belongs to $D$, and $y:\operatorname{Spec}\Omega\to Y$, $$\sum_a m_a\sum_{z:\ p_a z=x,\ f_a z=y}w_a(z)=0.$$ For every $n,i\in\mathbb Z$, the corresponding operators satisfy $$\sum_a m_a\,(p_a)_{*,w_a}\circ f_a^*=0:H^n_{\mathrm{et}}(Y,\mathbb Q_\ell(i))\longrightarrow H^n_{\mathrm{et}}(S,\mathbb Q_\ell(i)).$$

## Weighted trace after pullback is multiplication by degree

[Theorem AG.0676](https://andrewodesky.com/rh/lean/UpperTheory.Gal.TranscendenceTraces.trDegQ_holds/)

Assume the coefficient-restriction isomorphism for etale cohomology: restriction along any commutative-ring homomorphism preserves cohomology of every simplicial presheaf with coefficients in a sheaf over the target ring. Let $\ell$ be prime, let $p:Z\to S$ be a finite morphism of schemes, and let $w$ assign an integer to every geometric point of $Z$. Assume $\ell$ is invertible on $S$, that $w$ has the local constancy property below, and that for every geometric point $x$ of $S$, $$\sum_{z\in p^{-1}(x)}w(z)=d$$ for a fixed $d\in\mathbb Z$. For every $n,i\in\mathbb Z$, the weighted trace and pullback on rational $\ell$-adic etale cohomology satisfy $$\operatorname{Tr}_{p,w}\circ p^*=d\,\operatorname{id}:H^n(S,\mathbb Q_\ell(i))\to H^n(S,\mathbb Q_\ell(i)).$$

## Transitivity on embeddings of an integral closure

[Theorem ALG.0562](https://andrewodesky.com/rh/lean/UpperTheory.Gal.TranscendenceTraces.galTrans_holds/)

Let $A$ be an integrally closed commutative domain, let $K=\operatorname{Frac}A$, and let $L/K$ be a finite normal extension. Put $B=\overline A^{\,L}$, the integral closure of $A$ in $L$. Let $\Omega$ be a field and let $\phi,\phi':B\to\Omega$ be ring homomorphisms with equal restrictions to $A$. There is an $A$-algebra automorphism $g:B\xrightarrow{\sim}B$ such that $$\phi'(b)=\phi(g(b))\qquad(b\in B).$$
