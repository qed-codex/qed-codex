---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/GlobalInterpolation/ExistsOfFixedInt.lean",
  "declarations": [
    "GlobalTheory.UnramSelfDual.exists_frame"
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

## Orthonormal frames in unramified self-dual Hermitian lattices

[Theorem ANT.1269](https://andrewodesky.com/rh/lean/GlobalTheory.UnramSelfDual.exists_frame/)

Let $E/F$ be a CM quadratic extension with conjugation $\sigma$, and let $v$ be a finite prime of $F$ such that every prime of $E$ above $v$ has ramification index one. Put $E_v=F_v\otimes_FE$ and let $\mathcal O_v$ be the integral closure of $\mathcal O_{F_v}$ in $E_v$. Let $m\ge0$ and $J\in M_{m+1}(E)$ be nondegenerate and $\sigma$-Hermitian. Write $h(x,y)=\overline x^{\,t}Jy$ on $E_v^{m+1}$.

Let $L\subseteq E_v^{m+1}$ be a finitely generated $\mathcal O_v$-submodule spanning $E_v^{m+1}$ and satisfying $L=\{y:h(z,y)\in\mathcal O_v\text{ for all }z\in L\}$. There is $x\in L$ with $h(x,x)=1$. Every such $x$ extends to vectors $e_0,\ldots,e_m\in L$ with $$e_0=x,\qquad h(e_i,e_j)=\delta_{ij}.$$

**Inert places in theta data.** Let $F\subset E$ be number fields and $\sigma\colon E\to E$ an $F$-algebra homomorphism. Fix integers $a,a'\ge0$ and choose admissible base data and admissible geometric theta data of dimensions $(a,a')$ from ([Setting for theta lifts between unitary groups of a CM extension: base data, Hermitian data, Weil representations, theta integrals](https://andrewodesky.com/rh/lean/GlobalTheory.IndefiniteRowSideFullHecke.WeilTensorModels.Base.IsGood/)). Write $J'\in M_{a'}(E)$ and $L'\subset E^{a'}$ for the matrix and lattice of $V'$.

Let $v$ be a nonzero prime of $\mathcal O_F$ and $w$ a nonzero prime of $\mathcal O_E$ above $v$ such that $\mathfrak p_v\mathcal O_E=\mathfrak p_w$. Let $\sigma_w\colon E_w\to E_w$ be a ring homomorphism fixing $F_v$ and extending $\sigma$ on $E$, using the natural embeddings into the completions.

There exists $A\in\operatorname{GL}_{a'}(E_w)$ such that, writing $L'_w$ for the $\mathcal O_{E_w}$-span of the image of $L'$, $$A\mathcal O_{E_w}^{a'}=L'_w,\qquad A^tJ'\sigma_w(A)=I_{a'}.$$ The matrix $J'$ is viewed over $E_w$ and $\sigma_w$ acts entrywise.
