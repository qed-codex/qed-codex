---
{
  "module": "src/GroundTheory/HeightsAndTheta/Heights/OrbitLimits/PCurveCountLower.lean",
  "declarations": [
    "GroundTheory.Heights₂.Heights.Targets.CurveCountLower.proof"
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

## A linear lower bound for small sections on an arithmetic curve

[Theorem ARAK.1709](https://andrewodesky.com/rh/lean/GroundTheory.Heights%E2%82%82.Heights.Targets.CurveCountLower.proof/)

Assume the source's four arithmetic-curve input theorems: the vertical-plus-archimedean degree formula, the identification of a vertical degree with a logarithmic lattice index, linearity of those logarithmic indices, and the lattice-box counting lower bound.

Let $K$ be a nonempty finite set, $(I_k)$ finite coordinate sets, $\Omega$ a field, and $y=(y_{k,i})\in\Omega^{\bigsqcup_k I_k}$. Let $P$ be the kernel of the homomorphism $\mathbb Z[x_{k,i}]\to\Omega[T_k:k\in K]$ sending $x_{k,i}$ to $y_{k,i}T_k$. Assume $P$ is relevant, multihomogeneous and prime, $P\cap\mathbb Z=0$, and every element of $\Omega$ is $g(y)/h(y)$ for integral multihomogeneous polynomials $g,h$ of the same multidegree with $h(y)\ne0$.

Let $h_A$ be a positive metric function on the complex nonzero-block coordinate locus, of integer multidegree $a\in\mathbb Z^K$, so $h_A(cz)=\prod_k|c_k|^{a_k}h_A(z)$. Let $C_P$ be the complex zero set of $P$ with every block nonzero. For each choice of a coordinate $c_k\in I_k$ with $y_{k,c_k}\ne0$, put $R_c=\mathbb Z[y_{k,i}/y_{k,c_k}]\subseteq\Omega$. Define $$\Lambda_n=\left\{s\in\Omega:s\prod_k y_{k,c_k}^{-na_k}\in R_c\text{ for every such }c\right\}.$$ For $s\in\Omega$, $z\in C_P$ and $C\ge0$, write $B_n(s,z,C)$ for the inequalities $$|g(z)|\le C|h(z)|h_A(z)^n$$ for every pair of integral multihomogeneous polynomials $g,h$ with multidegree difference $na$ and $g(y)=s h(y)$. A section $s\in\Lambda_n$ is small if $B_n(s,z,1)$ for every $z\in C_P$.

Assume $\dim\mathbb Z[x]/P=1+|K|$, and $h_A$ is smooth and invariant under complex conjugation. Let $I$ be an arithmetic intersection system on all finite coordinate families, satisfying symmetry, additivity under tensor products of smooth metrics, and the rational-section recursion combining horizontal intersections, vertical degrees weighted by logarithms of residue characteristics, and archimedean logarithmic integrals. Denote its degree of the metrized multidegree $A=(a,h_A)$ on $P$ by $I(P;A)$. Then there is $C\in\mathbb R$ such that, for every integer $n\ge1$, $$nI(P;A)-C\le\log\operatorname{card}_{\mathbb N}\{s\in\Lambda_n:s\text{ is small}\}.$$ Here $\operatorname{card}_{\mathbb N}$ is ordinary finite cardinality and is defined to be zero on infinite sets; use $\log0=0$.
