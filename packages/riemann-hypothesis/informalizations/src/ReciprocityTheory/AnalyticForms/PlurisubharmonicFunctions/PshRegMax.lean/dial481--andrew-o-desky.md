---
{
  "module": "src/ReciprocityTheory/AnalyticForms/PlurisubharmonicFunctions/PshRegMax.lean",
  "declarations": [
    "ReciprocityTheory.AnForm.A.regMaxLevi_thm",
    "ReciprocityTheory.AnForm.A.regMax_thm"
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

## A smooth regularized maximum

[Theorem AG.0451](https://andrewodesky.com/rh/lean/ReciprocityTheory.AnForm.A.regMax_thm/)

Let $I$ be a finite nonempty set and let $\theta$ be the fixed normalized smooth even bump on $\mathbb R$ specified in the conventions, with inner radius $1/4$ and outer radius $1/2$. For $\eta>0$ and $t\in\mathbb R^I$, define $$M_\eta(t)=\int_{\mathbb R^I}\max_{i\in I}(t_i+\eta h_i)\prod_{i\in I}\theta(h_i)\,dh.$$ Then $M_\eta$ is smooth, convex, and nondecreasing in each coordinate, and $$\max_i t_i\le M_\eta(t)\le\max_i t_i+\eta/2.$$ If $t_j+\eta\le t_i$ for every $j\ne i$, then $M_\eta(t)=t_i$. If $j\ne k$, $t_j+\eta\le t_k$, and $s+\eta\le t_k$, replacing $t_j$ by $s$ does not change $M_\eta(t)$. For every $c\in\mathbb R$, $$M_\eta(t+c\mathbf1)=M_\eta(t)+c,\qquad\sum_{i\in I}\partial_iM_\eta(t)=1.$$ There is a real constant $C$, independent of $\eta,t,i,j$, such that $$|\partial_i\partial_jM_\eta(t)|\le C/\eta.$$

## Levi lower bounds under a regularized maximum

[Theorem AG.0486](https://andrewodesky.com/rh/lean/ReciprocityTheory.AnForm.A.regMaxLevi_thm/)

Let $U\subseteq\mathbb C^D$ be open, let $I$ be a finite nonempty set, let $\eta>0$, and let $u_j:\mathbb C^D\to\mathbb R$ be $C^2$ on $U$. Define $$M_\eta(t)=\int_{\mathbb R^I}\max_{j\in I}(t_j+\eta h_j)\prod_{j\in I}\kappa(h_j)\,dh.$$ For $z\in U$, $w\in\mathbb C^D$, and $a\in\mathbb R$, if $\mathcal L_{u_j}(z;w)\ge a$ for every $j$, then $$\mathcal L_{M_\eta((u_j)_j)}(z;w)\ge a.$$
