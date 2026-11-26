---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/TorsionLeftExactFunctorKernelSquareMatrixStatement.lean",
  "declarations": [
    "GlobalTheory.T.torsion_left_exact_functor_kernel_square_matrix"
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

## A torsion functor represented by the kernel of a square matrix

[Theorem GC.0952](https://andrewodesky.com/rh/lean/GlobalTheory.T.torsion_left_exact_functor_kernel_square_matrix/)

Let $\Lambda$ be a complete Noetherian commutative local ring with maximal ideal $\mathfrak m$ and finite residue field. Let $F$ be an additive $\Lambda$-linear endofunctor of $\Lambda$-modules. Call a module torsion here if each of its elements is annihilated by some power of $\mathfrak m$. Suppose:

- whenever $B'\xrightarrow{f}B\xrightarrow{g}B''$ is exact at $B$, $f$ is injective, and $B,B''$ are torsion, $F(f)$ is injective and $\operatorname{im}F(f)=\ker F(g)$;
- for each torsion $B$ and $y\in F(B)$, there is a finitely generated submodule $B'\subseteq B$ such that $y$ lies in the image of $F(B')\to F(B)$;
- for every exact sequence $0\to K\to B\to B''\to0$ with $K$ simple and $B$ torsion, both $F(K)$ and $F(B'')/\operatorname{im}(F(B)\to F(B''))$ are finite, and the cardinality of the latter is at most $|F(K)|$.

There are $a\ge0$ and $\Phi\in M_a(\Lambda)$ with every entry a nonunit such that, naturally for torsion $B$, $$F(B)\simeq_\Lambda\ker(\Phi:B^a\to B^a).$$ Naturality means these isomorphisms commute with every $\Lambda$-linear map between torsion modules.
