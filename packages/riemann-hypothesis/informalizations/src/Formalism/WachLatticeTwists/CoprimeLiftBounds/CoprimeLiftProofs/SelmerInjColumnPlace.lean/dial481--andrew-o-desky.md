---
{
  "module": "src/Formalism/WachLatticeTwists/CoprimeLiftBounds/CoprimeLiftProofs/SelmerInjColumnPlace.lean",
  "declarations": [
    "Formalism.RepresentationBoundsCohomology.BR.selmer_inj_tensor_form"
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

## Independence after passing from lattice cocycles to torsion coefficients

[Theorem GC.1105](https://andrewodesky.com/rh/lean/Formalism.RepresentationBoundsCohomology.BR.selmer_inj_tensor_form/)

Let $O$ be a discrete valuation domain, $K=\operatorname{Frac}O$, $D$ a group, and $$0\longrightarrow L\xrightarrow{i}V\xrightarrow{q}M\longrightarrow0$$ an exact sequence of $O[D]$-modules, where $V$ is also a $K$-vector space and its $D$-action is $K$-linear. Assume every $v\in V$ has a nonzero $c\in O$ with $cv\in i(L)$. Fix an $O$-bilinear map $b:L\times(K/O)\to M$ with $b(v,\bar x)=q(xi(v))$.

Let $F\subseteq H^1(D,L)$ be saturated: $cz\in F$ and $c\ne0$ imply $z\in F$. Let $\kappa_1,\ldots,\kappa_j$ be cocycles whose classes lie in $F$. Assume every $z\in F$ differs from an $O$-linear combination of these classes by a class killed by some nonzero element of $O$, and that $$c\sum_a u_a[\kappa_a]=0,\quad c\ne0\quad\Longrightarrow\quad u_a=0\text{ for every }a.$$ If $x_a\in K/O$ and $m\in M$ satisfy $$\sum_a b(\kappa_a(g),x_a)=g m-m\qquad(g\in D),$$ then $x_a=0$ for every $a$.
