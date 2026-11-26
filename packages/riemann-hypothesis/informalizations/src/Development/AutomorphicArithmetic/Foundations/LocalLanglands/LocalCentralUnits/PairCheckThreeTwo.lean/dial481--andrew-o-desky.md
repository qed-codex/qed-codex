---
{
  "module": "src/Development/AutomorphicArithmetic/Foundations/LocalLanglands/LocalCentralUnits/PairCheckThreeTwo.lean",
  "declarations": [
    "UpperTheory.Zero.LLC.pin"
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

## Frobenius character sums determine a regular character

[Theorem ALG.1725](https://andrewodesky.com/rh/lean/UpperTheory.Zero.LLC.pin/)

Let $p$ be prime, $n\ge1$, and $K/\mathbb F_p$ a field extension of degree $n$. A multiplicative character $\theta:K^\times\to\mathbb C^\times$ is regular if its orbit under $\theta\mapsto\theta^p$ has size $n$. For a regular $\theta$, put $$S_\theta(z)=\sum_{j=0}^{n-1}\theta(z^{p^j}).$$ There exists $z\in K^\times$ with $[\mathbb F_p(z):\mathbb F_p]=n$ and $S_\theta(z)\ne0$. Moreover, if $\theta'$ is regular and $S_\theta(z)=S_{\theta'}(z)$ for every such full-degree $z$, then $$\theta'=\theta^{p^j}\quad\text{for some }0\le j<n.$$
