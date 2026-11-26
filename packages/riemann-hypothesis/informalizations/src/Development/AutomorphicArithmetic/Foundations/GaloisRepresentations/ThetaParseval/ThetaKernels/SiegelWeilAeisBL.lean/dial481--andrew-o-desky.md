---
{
  "module": "src/Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/ThetaParseval/ThetaKernels/SiegelWeilAeisBL.lean",
  "declarations": [
    "PositivityTheory.SiegelWeilFormula.Aeis.eisBLW_k"
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

## Weak meromorphic continuation of Siegel Eisenstein series

[Theorem THETA.1168](https://andrewodesky.com/rh/lean/PositivityTheory.SiegelWeilFormula.Aeis.eisBLW_k/)

Let $E/F$ be number fields with involution $\sigma$, and fix the source's good CM base data $\mathcal B$. Let $Y$ be its space datum of rank $n\ge1$, $G$ the associated doubled group, $P$ its Siegel parabolic, and $b$ an allowed Siegel frame. Let $K\subset G$ be the standard compact subgroup in that frame, and let $a:G\to\mathbb R$ be a height satisfying Iwasawa decomposition $g=pk$ and $a(pk)=|\det t|_{\mathbb A_E}$ for the Levi component $t$ of $p$. Let $\chi:\mathbb A_E^\times\to S^1$ be a continuous character trivial on $E^\times$, with restriction to $\mathbb A_F^\times$ equal to $\eta_{E/F}^{c}$ for some $c\ge0$, where $\eta_{E/F}$ is the quadratic character with kernel $F^\times N_{E/F}(\mathbb A_E^\times)$. Let $f:G\to\mathbb C$ be continuous, $K$-finite under right translation, and satisfy $$f(pg)=\chi(\det t)|\det t|_{\mathbb A_E}^{s_1+n/2}f(g)\qquad(s_1\in\mathbb C).$$ Then there exists $\widehat E:\mathbb C\times G\to\mathbb C$ and $t\in\mathbb R$ such that, for $\operatorname{Re}s>t$ and every $g$, the series $$\sum_{\gamma\in P(F)\backslash G(F)}a(\gamma g)^{s-s_1}f(\gamma g)$$ converges unconditionally to $\widehat E(s,g)$, and $s\mapsto\widehat E(s,g)$ is holomorphic there. For every $s_0\in\mathbb C$, there exist $k\ge0$, a neighborhood $U$ of $s_0$, and a map $H:U\to\mathcal M(G)$ such that $$H(s)(g)=(s-s_0)^k\widehat E(s,g)\qquad(s\in U,\ s\ne s_0).$$ Here $\mathcal M(G)$ is the span of continuous functions bounded in norm by some integer power of the prescribed group height. For every complex-linear functional $\lambda$ on $\mathcal M(G)$ bounded on each class of functions satisfying $|h(g)|\le\operatorname{ht}(g)^N$, the function $s\mapsto\lambda(H(s))$ is holomorphic on $U$.
