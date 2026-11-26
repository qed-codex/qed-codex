---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsSemiAbelianExtensionNearPointStatement.lean",
  "declarations": [
    "GlobalTheory.T.exists_semiAbelianExtension_near_point"
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

## A semiabelian extension on a neighborhood of each boundary point

[Theorem AV.1548](https://andrewodesky.com/rh/lean/GlobalTheory.T.exists_semiAbelianExtension_near_point/)

Let $S$ be a normal Noetherian scheme, $j:X\hookrightarrow S$ a dominant open immersion, and $A\to X$ an abelian scheme with a relatively ample line bundle.

Suppose that for every $x\in S$ there are data with the following properties:

1. A regular local domain $R$ of characteristic zero, complete for its maximal ideal $\mathfrak m_R$, and a morphism $\xi:\operatorname{Spec}R\to S$ sending the closed point to $x$.
2. The induced local homomorphism $\phi:\mathcal O_{S,x}\to R$ is flat and satisfies $\mathfrak m_x R=\mathfrak m_R$. The composite $\mathcal O_{S,x}\xrightarrow{\phi}R\to R/\mathfrak m_R$ is finite and formally unramified.
3. A semiabelian group scheme $G\to\operatorname{Spec}R$. Writing $K=\operatorname{Frac}R$ and $\eta_R:\operatorname{Spec}K\to\operatorname{Spec}R$ for the generic-point morphism, there are a morphism $y:\operatorname{Spec}K\to X$ with $j\circ y=\xi\circ\eta_R$ and a group-scheme isomorphism $G_K\simeq y^*A$.

Then for every $s\in S$ there are an open neighborhood $U\subseteq S$ of $s$ and a semiabelian group scheme $G_U\to U$ whose pullback to $j^{-1}(U)$ is isomorphic to $A|_{j^{-1}(U)}$ as a group scheme.
