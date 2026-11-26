---
{
  "module": "src/Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/BasicOpenSections/EsGenAll.lean",
  "declarations": [
    "UpperTheory.Gal.Mod.esGen_all",
    "UpperTheory.Gal.Mod.specGood"
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

## A Frobenius polynomial identity on the generic fiber

[Theorem GC.0070](https://andrewodesky.com/rh/lean/UpperTheory.Gal.Mod.esGen_all/)

Let $\ell,p$ be primes, $f,n\ge0$, and $q=p^f$. Let $O$ be a discrete valuation ring with uniformizer $\varpi$ in which $p$ is not a unit. Let $K,\kappa$ be $O$-algebra fields with $p\ne0$ in $K$, $\varpi=0$ in $\kappa$, and $a^q=a$ for all $a\in\kappa$. Choose algebraically closed extensions $\Omega/K$, $\bar\kappa/\kappa$, a valuation ring $V\subset\Omega$ containing the image of $O$, and a surjective ring map $r:V\to\bar\kappa$ compatible with the two maps from $O$. Assume $\ell$ is invertible in $\bar\kappa$.

Let $Y/O$ be smooth and proper. For $j=0,\ldots,n$, take a correspondence $Y\xleftarrow{a_j} Z_j\xrightarrow{b_j}Y$ with $a_j$ finite, etale where $p$ is invertible, and of constant degree on algebraically closed fibers in which $p$ is nonzero; require both maps to have the same composite to $\operatorname{Spec}O$. Assume the alternating geometric-point identity specified in the conventions for this family at generic points of the special fiber. On the geometric generic fiber, choose the base-changed correspondences with weight one and write $T_j$ for their induced operators on rational etale cohomology.

For every automorphism $\gamma\in\operatorname{Aut}_K\Omega$ preserving $V$ and every cohomological degree $k\in\mathbb Z$, let $R_k(\gamma)$ be its action on $H^k_{\mathrm{et}}(Y_\Omega,\mathbb Q_\ell)$. If $r(\gamma v)=r(v)$ for all $v\in V$, then $R_k(\gamma)=1$. If $r(\gamma v)=r(v)^q$ for all $v\in V$, then $$\sum_{j=0}^n(-1)^j q^{\binom j2}T_jR_k(\gamma^{-1})^{n-j}=0.$$

## Specialization of smooth proper etale cohomology

[Theorem AG.0092](https://andrewodesky.com/rh/lean/UpperTheory.Gal.Mod.specGood/)

Let $O$ be a commutative ring with maps to fields $K$ and $\kappa$. Let $\Omega,\overline\kappa$ be algebraically closed extensions of $K,\kappa$, respectively. Let $V\subset\Omega$ be a valuation subring containing the image of $O$, and let $r:V\twoheadrightarrow\overline\kappa$ be a surjective ring map compatible with the maps from $O$. Let $Y\to\operatorname{Spec}O$ be smooth and proper. Write $Y_V,Y_\Omega,Y_{\overline\kappa}$ for its base changes, and fix morphisms $i:Y_{\overline\kappa}\to Y_V$ and $j:Y_\Omega\to Y_V$ over $Y$ and the maps induced by $r$ and $V\hookrightarrow\Omega$.

For every $q\ge0$ invertible in $\overline\kappa$ and $a\in\mathbb Z$, both morphisms induce isomorphisms on etale cohomology with coefficients $\mathbb Z/q\mathbb Z(a)$ in every degree. For every prime $\ell$ invertible in $\overline\kappa$ and $n,a\in\mathbb Z$, there is an isomorphism $$\operatorname{sp}:H^n_{\mathrm{et}}(Y_{\overline\kappa},\mathbb Q_\ell(a))\simeq H^n_{\mathrm{et}}(Y_\Omega,\mathbb Q_\ell(a)),\qquad\operatorname{sp}\circ i^*=j^*.$$ For $\sigma\in\operatorname{Aut}_K(\Omega)$ and $\tau\in\operatorname{Aut}_\kappa(\overline\kappa)$ with $\sigma(V)\subset V$ and $r\sigma=\tau r$ on $V$, this satisfies $\operatorname{sp}(\tau^*x)=\sigma^*\operatorname{sp}(x)$.
