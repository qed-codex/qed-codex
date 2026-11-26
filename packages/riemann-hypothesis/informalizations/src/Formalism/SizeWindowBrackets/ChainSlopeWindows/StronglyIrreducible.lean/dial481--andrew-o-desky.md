---
{
  "module": "src/Formalism/SizeWindowBrackets/ChainSlopeWindows/StronglyIrreducible.lean",
  "declarations": [
    "Formalism.LFunctionChainParameters.characterSumData.colour_sum",
    "Formalism.LFunctionChainParameters.characterSumData.orthogonality_ramified"
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

## Character sum on the complementary coset

[Theorem ANT.0153](https://andrewodesky.com/rh/lean/Formalism.LFunctionChainParameters.characterSumData.colour_sum/)

Let $H$ be a finite abelian group, written additively, put $G=(\mathbb Z/2\mathbb Z)^2\times H$, and set $$\Phi=\{((\alpha,\beta),h):\alpha=0\},\qquad\chi_C((\alpha,\beta),h)=(-1)^\alpha.$$ For every complex character $\chi\in\widehat G$, $$\sum_{g\in G\setminus\Phi}\overline{\chi(g)}=\begin{cases}|\Phi|,&\chi=1,\\-|\Phi|,&\chi=\chi_C,\\0,&\chi\ne1,\chi_C.\end{cases}$$ Here $1$ is the trivial character, and $\chi_C\ne1$.

## Fourier orthogonality for inertia averages

[Theorem ANT.0154](https://andrewodesky.com/rh/lean/Formalism.LFunctionChainParameters.characterSumData.orthogonality_ramified/)

Let $H$ be a finite abelian group, written additively, let $G=(\mathbb Z/2\mathbb Z)^2\times H$, and put $\Phi=\{((\alpha,\beta),h):\alpha=0\}$. For each natural number $r$, choose a subgroup $I_r\subseteq G$ and an element $F_r\in G$. For a complex character $\chi\in\widehat G$ and an integer $n\ge1$, define $$a_\chi(n)=\prod_{\substack{r\mid n\\r\ \mathrm{prime}}}\frac1{|I_r|}\sum_{z\in I_r}\chi(v_r(n)F_r+z),$$ where $v_r(n)$ is the exponent of $r$ in $n$ and an empty product is $1$. For every prime $p$, every integer $i\ge1$, and every $g\in G$, $$\frac1{|\Phi|}\sum_{\chi\in\widehat G}\overline{\chi(g)}\,a_\chi(p^i)=\begin{cases}2/|I_p|,&g-iF_p\in I_p,\\0,&g-iF_p\notin I_p.\end{cases}$$
