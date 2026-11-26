---
{
  "module": "src/GroundTheory/HeightsAndTheta/Heights/HilbertSamuel/StatementsArithKleiman.lean",
  "declarations": [
    "GroundTheory.Heights₂.Heights.HilbertSamuel.ArithKleiman.Statement"
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

## Three arithmetic intersection and small-section hypotheses

[Definition / hypothesis ARAK.D015](https://andrewodesky.com/rh/lean/GroundTheory.Heights%E2%82%82.Heights.HilbertSamuel.ArithKleiman.Statement/)

The following are three hypotheses about the coordinates, arithmetic varieties and basic intersection systems of ([Arithmetic intersection systems in homogeneous coordinates](https://andrewodesky.com/rh/lean/ReciprocityTheory.ChartRestriction.G.Geo.IsIntersectionSystem/)), and the positivity conditions, chart lattices, small sections and real volumes of ([Small sections and positivity in homogeneous coordinates](https://andrewodesky.com/rh/lean/ReciprocityTheory.ChartRestriction.G.Geo.Birational/)). Each hypothesis is quantified over all finite block and coordinate sets and every basic intersection system $I$.

**1. Nonnegativity of top self-intersections.** Let $D\in\mathbb N$, let $P$ be an arithmetic variety of dimension $D+1$, let $P_0\subseteq P$ be an ideal, and let $A=(a,h)$ be a Hermitian line datum. Suppose $A$ is semipositive relative to $P_0$ on $P$, invariant under conjugation, and nef on the fibres of $P$. Suppose also $$I_W(A)\ge0$$ for every arithmetic variety $W$ of dimension $1$ with $P\subseteq W$. Then $$I_P(\underbrace{A,\ldots,A}_{D+1})\ge0.$$

**2. Upper bound from small generators.** Let $\Omega$ be a field of characteristic zero, let $y$ be birational coordinates in $\Omega$, and suppose $P=P_y$ is an arithmetic variety of dimension $D+1$, where $D\ge1$ is an integer. Let $P_0\subseteq P$, and let $A=(a,h)$ be semipositive relative to $P_0$ on $P$ and invariant under conjugation. Impose the following two further conditions.

First, require the degree defined in ([Degrees from multigraded Hilbert functions](https://andrewodesky.com/rh/lean/GroundTheory.Heights%E2%82%82.Heights.HilbertSamuel.genDeg/)) to satisfy $$\deg_D(P,a)>0.$$

Second, there are finitely many $w_1,\ldots,w_q\in\mathcal B_1(y,A)$ such that for every coordinate choice $c$ with all $y_{b,c_b}\ne0$ there are $u_1,\ldots,u_q\in R_c$ satisfying $$\sum_{j=1}^q u_j\left(w_j\prod_b y_{b,c_b}^{-a_b}\right)=1.$$ Then $$V_D(y,A)\le I_P(\underbrace{A,\ldots,A}_{D+1}).$$

**3. Upper bound with integral closure.** Let $\Omega$ be any field, let $y$ be birational coordinates in $\Omega$, and suppose $P=P_y$ is an arithmetic variety of dimension $D+1$, where $D\ge1$ is an integer. Let $P_0\subseteq P$ and let $A=(a,h)$ have $a\in\mathbb N^B$. If $A$ is semipositive relative to $P_0$ on $P$, invariant under conjugation and satisfies the monomial bound, then $$V_D^\nu(y,A)\le I_P(\underbrace{A,\ldots,A}_{D+1}).$$

The *three arithmetic intersection and small-section hypotheses* mean the conjunction of assertions 1–3.
