---
{
  "module": "src/Development/AutomorphicArithmetic/PrimitiveCosets/TopsSum.lean",
  "declarations": [
    "UpperTheory.Comparison₂.tops_sum"
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

## Coset proportions and character averages

[Theorem ALG.0155](https://andrewodesky.com/rh/lean/UpperTheory.Comparison%E2%82%82.tops_sum/)

Let $H$ be a finite abelian group and $H_0\le H$ a subgroup of index $o$. Let $T\subset H$, and let $b_0,c_0,\eta\in\mathbb R$. Suppose $\vartheta:H\to\mathbb C^\times$ is a nontrivial character trivial on $H_0$, and assume, for every $h\in H$, $$\left||T\cap(h+H_0)|-\{b_0+c_0\mathbf1_{H_0}(h)\}\right|\le\eta.$$ Then $$\left|\sum_{t\in T}\vartheta(t)-c_0\right|\le o\eta.$$

In the application, put $G=(\mathbb Z/2\mathbb Z)^2\times H$, $b_0=3|T|/(3o+1)$, $c_0=|T|/(3o+1)$ and $\eta=\delta|T|$, with $\delta\in\mathbb R$. If $\gamma\in\widehat G$ is trivial on $\{0\}\times H_0$ and nontrivial on $\{0\}\times H$, the hypothesis becomes $$\left||T\cap(h+H_0)|-\lambda(h)|T|\right|\le\delta|T|,\qquad \lambda(h)=\begin{cases}4/(3o+1),&h\in H_0,\\3/(3o+1),&h\notin H_0.\end{cases}$$ Its conclusion is $$\left|\sum_{t\in T}\gamma(0,t)-\frac{|T|}{3o+1}\right|\le o\delta|T|.$$
