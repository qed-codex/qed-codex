---
{
  "module": "src/Development/WeilBound/RepresentationTheoryGL/GenericUnitaryGL/ComplementarySeries/PosMkIff.lean",
  "declarations": [
    "PositivityTheory.RgGu.NR.Sig.lim_form",
    "PositivityTheory.RgGu.NR.Sig.pos_of"
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

## A nondegenerate semidefinite Hermitian form is positive definite

[Theorem ALG.1478](https://andrewodesky.com/rh/lean/PositivityTheory.RgGu.NR.Sig.pos_of/)

Let $W$ be a finite-dimensional complex vector space and let $B:W\times W\to\mathbb C$ be linear in its first variable and conjugate-linear in its second. Suppose $B(v,w)=\overline{B(w,v)}$, $\{v:B(v,w)=0\text{ for every }w\}={0\}$, and $\operatorname{Re}B(v,v)\ge0$ for every $v\in W$. Then $$\operatorname{Re}B(v,v)>0\qquad(v\ne0).$$

## Limits of normalized invariant Hermitian forms

[Theorem ALG.1505](https://andrewodesky.com/rh/lean/PositivityTheory.RgGu.NR.Sig.lim_form/)

Let $W$ be a finite-dimensional complex vector space with a fixed basis $e_1,\ldots,e_d$. Let $I$ be a set, $\iota:I\to I$ a map, and $T:\mathbb R\times I\to\operatorname{End}_{\mathbb C}W$ satisfy: for all $i,v$ and linear functionals $\lambda$, $s\mapsto\lambda(T(s,i)v)$ is continuous. Let $s_k\to p$ and let $B_k$ be sesquilinear forms, linear in the first argument, such that $$B_k(T(s_k,i)v,w)=B_k(v,T(s_k,\iota(i))w),\qquad B_k(w,v)=\overline{B_k(v,w)}.$$ Assume their Gram matrices $G_k=(B_k(e_a,e_b))$ have norm one, using the supremum of the absolute values of their entries. There exist a strictly increasing $\varphi:\mathbb N\to\mathbb N$ and a matrix $G$ of norm one such that $G_{\varphi(k)}\to G$. The form $B$ with Gram matrix $G$ is Hermitian, satisfies $$B(T(p,i)v,w)=B(v,T(p,\iota(i))w),$$ and $B_{\varphi(k)}(v,w)\to B(v,w)$ for every $v,w$.
