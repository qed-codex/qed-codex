---
{
  "module": "src/Development/AutomorphicSpectrum/Proofs/MetricProofs/RegularizationGlueC2ExplicitStatement.lean",
  "declarations": [
    "GlobalTheory.T.regularization_glue_C2_explicit"
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

## Gluing local plurisubharmonic approximations with C2 convergence

[Theorem AG.1178](https://andrewodesky.com/rh/lean/GlobalTheory.T.regularization_glue_C2_explicit/)

Let $X$ be compact Hausdorff with compatible finite holomorphic atlases $A,B$ of complex dimension $e$. Write $B_j(r)$ for the inverse image under the $j$th chart of the open radius-$r$ ball in $\mathbb C^e$. Assume the sets $B_j(1)$ cover $X$ and every $B$-chart target contains the closed radius-two ball. Let $\Theta,\theta$ be smooth local potential systems for $A$, with differences locally real parts of holomorphic functions, and assume the Levi form of $\Theta$ is positive definite. Let $s:X\times X\to\mathbb C$ have closed set $Z=\{y:s(y,y)=0\}$, and let $\varphi:X\to\mathbb R$ be smooth off $Z$.

There is $K>0$ with the following property. Let $t_0>0$, $\delta:\mathbb R\to\mathbb R$ tend to zero as $t\downarrow0$, and let $f_{t,j}:X\to\mathbb R$. For $0<t\le t_0$, suppose $t\le\delta(t)\le1$, each $f_{t,j}$ is smooth on $B_j(5/4)$, the functions are bounded there by a common finite bound for that $t$, $\theta+f_{t,j}$ is plurisubharmonic there, and $$|f_{t,j}-f_{t,k}|\le\delta(t)\quad\text{on }B_j(5/4)\cap B_k(5/4).$$ Assume that in each $B$-chart $f_{t,j}$ and its first two real derivatives converge uniformly to those of $\varphi$ on every compact subset of the radius-$5/4$ ball outside $Z$, with first derivative error $O(t)$ on each such compact subset. Then there exist functions $F_t:X\to\mathbb R$, smooth for $0<t\le t_0$, such that $$\theta+F_t+K\delta(t)\Theta\ \text{is plurisubharmonic},\qquad f_{t,j}\le F_t\le f_{t,j}+K\delta(t)\quad\text{on }B_j(5/4).$$ In every $A$-chart, $F_t\to\varphi$ with its first two real derivatives uniformly on compact subsets outside $Z$ as $t\downarrow0$.
