---
{
  "module": "src/Development/AutomorphicSpectrum/Proofs/GeometryProofs/ComplexPointExistsUniqueEmbeddingStatement.lean",
  "declarations": [
    "GlobalTheory.T.complex_point_existsUnique_embedding"
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

## A complex point determines a unique embedding of the base number field

[Theorem AG.1081](https://andrewodesky.com/rh/lean/GlobalTheory.T.complex_point_existsUnique_embedding/)

Let $B,I_b$ be finite sets, $\Omega$ a field, $F$ a number field, $\phi:F\hookrightarrow\Omega$, and $y=(y_{b,i})\in\Omega^{\coprod_b I_b}$. Assume every block has a nonzero coordinate and, for every choice $c_b$ with $y_{b,c_b}\ne0$, the ring $$\mathbb Z[y_{b,i}/y_{b,c_b}:b\in B,i\in I_b]$$ contains $\phi(\mathcal O_F)$.

Let $P_y$ be the kernel of $\mathbb Z[X_{b,i}]\to\Omega[T_b]$, $X_{b,i}\mapsto y_{b,i}T_b$. For every complex tuple $z$ whose blocks are nonzero and on which all elements of $P_y$ vanish, there is a unique embedding $\sigma:F\hookrightarrow\mathbb C$ with the following property. For every $a\in F$ and every pair of integral polynomials $g,h$ multihomogeneous of the same multidegree, $$g(y)=\phi(a)h(y)\quad\Longrightarrow\quad g(z)=\sigma(a)h(z).$$
