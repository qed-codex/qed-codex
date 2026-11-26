---
{
  "module": "src/ReciprocityTheory/ReductiveGroups/ArithmeticGeometry/PlaceDivisors/AlWellDefSt.lean",
  "declarations": [
    "ReciprocityTheory.ChartRestriction.G.Pdiv.IsAl",
    "ReciprocityTheory.ChartRestriction.G.Pdiv.IsCharTors",
    "ReciprocityTheory.ChartRestriction.G.Pdiv.LieG",
    "ReciprocityTheory.ChartRestriction.G.Pdiv.Tv",
    "ReciprocityTheory.ChartRestriction.G.Pdiv.omega"
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

## Compatible torsion characters and logarithmic differentials

[Definition / hypothesis PHT.D098](https://andrewodesky.com/rh/lean/ReciprocityTheory.ChartRestriction.G.Pdiv.Tv/)

Compatible characters on torsion subschemes have logarithmic differentials characterized by their values on infinitesimal points.

**Tangent vectors and linear functions.** Let $O$ be a commutative ring and let $G$ be a group scheme over $O$. Put $O_\varepsilon=O[\varepsilon]/(\varepsilon^2)$. The tangent vectors at the identity form the set $$\operatorname{Lie}_O(G)=\ker\bigl(G(O_\varepsilon)\longrightarrow G(O)\bigr).$$ The map is induced by $\varepsilon\mapsto0$, and the kernel is taken at the identity of $G(O)$. For tangent vectors, write $x+y$ for multiplication of the corresponding points of $G(O_\varepsilon)$ and $ax$ for the image under $\varepsilon\mapsto a\varepsilon$, for $a\in O$. Let $\Omega(G)$ be the $O$-module of functions $f:\operatorname{Lie}_O(G)\to O$ satisfying $$f(x+y)=f(x)+f(y),\qquad f(ax)=a f(x)\quad(a\in O).$$ Its operations are pointwise.

**Compatible torsion characters.** Fix $p\in\mathbb N$. For each $N\in\mathbb N$, write $G[N]$ for the fibre over the identity of the power map $g\mapsto g^N$ on $G$. A compatible torsion character is a sequence of morphisms of $O$-schemes $$\chi_n:G[p^n]\longrightarrow\mathbb G_{m,O}\qquad(n\ge0)$$ with the following two properties. For every $n$, every $O$-scheme $T$, and all $x,y,z\in G[p^n](T)$ whose images satisfy $z=xy$ in $G(T)$, require $\chi_n(z)=\chi_n(x)\chi_n(y)$. Also require $\chi_{n+1}$ to restrict to $\chi_n$ on $G[p^n]$ under its natural inclusion in $G[p^{n+1}]$.

**Logarithmic differential.** Suppose $O$ is complete and separated for the $(p)$-adic topology. The logarithmic differential of $\chi=(\chi_n)_n$ is the unique element $d\log\chi\in\Omega(G)$ with the following property.

For every $n\in\mathbb N$, every commutative $O$-algebra $R$ in which $p^n=0$, every $x\in\operatorname{Lie}_O(G)$, and every $$w\in G[p^n]\bigl(R[\varepsilon]/(\varepsilon^2)\bigr)$$ whose image in $G(R[\varepsilon]/(\varepsilon^2))$ is the base change $x_R$ of $x$, one has $$\chi_n(w)=1+\varepsilon\,\iota_R\bigl((d\log\chi)(x)\bigr).$$ Here $\iota_R:O\to R$ is the structure homomorphism, and the equality is in $(R[\varepsilon]/(\varepsilon^2))^\times$.
