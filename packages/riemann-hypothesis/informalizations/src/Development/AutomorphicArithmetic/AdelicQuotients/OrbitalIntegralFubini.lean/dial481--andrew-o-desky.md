---
{
  "module": "src/Development/AutomorphicArithmetic/AdelicQuotients/OrbitalIntegralFubini.lean",
  "declarations": [
    "UpperTheory.orbital_integral_fubini"
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

## Interchanging a real integral with a twisted orbital integral

[Theorem REP.0483](https://andrewodesky.com/rh/lean/UpperTheory.orbital_integral_fubini/)

Let $G,T$ be second-countable locally compact Hausdorff groups with their Borel measurable structures and inversion-invariant Haar measures $\mu,\nu$. Let $j:T\to G$ be a group homomorphism that is a closed embedding. Let $\theta:G\to G$ be a continuous homomorphism, let $\delta\in G$, and let $z:\mathbb R\to G$ be continuous. Put $a(x)=x^{-1}\delta\theta(x)$ and suppose $a(j(t))=\delta$ for every $t\in T$.

Assume that for every compact $D\subseteq G$ there are compact sets $C\subseteq G$, $B\subseteq\mathbb R$ such that $$a(x)\in D\Longrightarrow x\in j(T)C,\qquad z(s)a(x)\in D\Longrightarrow s\in B.$$ For every continuous compactly supported $\varphi:G\to\mathbb C$, the function $x\mapsto\int_{\mathbb R}\varphi(z(s)a(x))\,ds$ is measurable, and $$Q\!\left(x\mapsto\int_{\mathbb R}\varphi(z(s)a(x))\,ds\right)=\int_{\mathbb R}Q\!\left(x\mapsto\varphi(z(s)a(x))\right)\,ds.$$
