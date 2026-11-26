---
{
  "module": "src/Development/AutomorphicArithmetic/AdelicQuotients/AdelicGLSplitEquiv.lean",
  "declarations": [
    "UpperTheory.adelicGL_split_equiv"
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

## A central section gives a direct-product homeomorphism

[Theorem ALG.0422](https://andrewodesky.com/rh/lean/UpperTheory.adelicGL_split_equiv/)

Let $G$ be a topological group and let $G_1,R$ be groups equipped with topologies. Suppose homomorphisms $$i:G_1\to G,\qquad d:G\to R,\qquad c:R\to G$$ satisfy: $i$ is a topological embedding; $d,c$ are continuous; $d\circ c=\operatorname{id}_R$; every $c(s)$ is central in $G$; and $\ker d=i(G_1)$. Then $$G_1\times R\longrightarrow G,\qquad(x,s)\longmapsto i(x)c(s)$$ is a group isomorphism and a homeomorphism.
