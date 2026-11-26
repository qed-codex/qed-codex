---
{
  "module": "src/GroundTheory/HeightsAndTheta/Heights/HilbertSamuel/IsMultiHomogSumSmulMap.lean",
  "declarations": [
    "GroundTheory.Heights₂.Heights.HilbertSamuel.SectionL2Lattice.proof"
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

## Euclidean lattices from L2 norms of arithmetic sections

[Theorem ARAK.1712](https://andrewodesky.com/rh/lean/GroundTheory.Heights%E2%82%82.Heights.HilbertSamuel.SectionL2Lattice.proof/)

Assume the source's five section-lattice input theorems: normalized pointwise section values, real independence of values, realization of an L2 Gram form as a Euclidean lattice, polynomial rank bounds on sections of the normalization, and finite supremum bounds on sections.

Let $K$ be a nonempty finite set, $(I_k)$ finite coordinate sets, $\Omega$ a field, and $y=(y_{k,i})\in\Omega^{\bigsqcup_k I_k}$. Let $P$ be the kernel of the homomorphism $\mathbb Z[x_{k,i}]\to\Omega[T_k:k\in K]$ sending $x_{k,i}$ to $y_{k,i}T_k$. Assume $P$ is relevant, multihomogeneous and prime, $P\cap\mathbb Z=0$, and every element of $\Omega$ is $g(y)/h(y)$ for integral multihomogeneous polynomials $g,h$ of the same multidegree with $h(y)\ne0$.

Let $h_A$ be a positive metric function on the complex nonzero-block coordinate locus, of integer multidegree $a\in\mathbb Z^K$, so $h_A(cz)=\prod_k|c_k|^{a_k}h_A(z)$. Let $C_P$ be the complex zero set of $P$ with every block nonzero. For each choice of a coordinate $c_k\in I_k$ with $y_{k,c_k}\ne0$, put $R_c=\mathbb Z[y_{k,i}/y_{k,c_k}]\subseteq\Omega$. Define $$\Lambda_n=\left\{s\in\Omega:s\prod_k y_{k,c_k}^{-na_k}\in R_c\text{ for every such }c\right\}.$$ For $s\in\Omega$, $z\in C_P$ and $C\ge0$, write $B_n(s,z,C)$ for the inequalities $$|g(z)|\le C|h(z)|h_A(z)^n$$ for every pair of integral multihomogeneous polynomials $g,h$ with multidegree difference $na$ and $g(y)=s h(y)$. A section $s\in\Lambda_n$ is small if $B_n(s,z,1)$ for every $z\in C_P$.

Assume also $\operatorname{char}\Omega=0$, $\dim\mathbb Z[x]/P=D+1+|K|$, and $h_A$ is continuous. Let $\mu$ be a probability measure on the full complex coordinate space supported on $C_P$, and suppose every complex multihomogeneous polynomial vanishing $\mu$-almost everywhere vanishes on all of $C_P$. Put $$p_n(s,z)=\inf\{C\ge0:B_n(s,z,C)\},$$ taking this infimum to be zero when the set is empty. There are integers $r_n\ge0$ and injective additive maps $\phi_n:\Lambda_n\to\mathbb R^{r_n}$ such that their images are discrete full $\mathbb Z$-lattices and $$\|\phi_n(s)\|=\left(\int p_n(s,z)^2\,d\mu(z)\right)^{1/2}.$$ If $C\ge0$ and $B_n(s,z,C)$ holds for all $z\in C_P$, then $\|\phi_n(s)\|\le C$. If $t\in\Lambda_k$ is small and $st\in\Lambda_{n+k}$, then $$\|\phi_{n+k}(st)\|\le\|\phi_n(s)\|.$$ Finally, there is $C_0\in\mathbb R$ with $r_n\le C_0(n+1)^D$ for every $n\ge0$.
