---
{
  "module": "src/Development/WeilBound/RepresentationTheoryGL/HolomorphicDiscreteSeries/HarishChandraDescent/FarClosed.lean",
  "declarations": [
    "PositivityTheory.RgHe3.far_closed"
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

## Discrete series in a restriction at large parameters

[Theorem REP.1584](https://andrewodesky.com/rh/lean/PositivityTheory.RgHe3.far_closed/)

Let $\epsilon\in\{\pm1\}^{n+1}$, $\epsilon'\in\{\pm1\}^{n}$, and fix a coordinate embedding $j:U(\epsilon')\hookrightarrow U(\epsilon)$ whose omitted coordinate has sign $+1$ and whose other signs agree. Write $\widetilde Y$ for a matrix $Y\in M_n(\mathbb C)$ embedded in those coordinates, with zero in the omitted coordinate. Let $\lambda,d\in\mathbb R^{n+1}$, $d'\in\mathbb R^n$, and $g\in U(\epsilon)$ satisfy $$\operatorname{tr}(\operatorname{diag}(d)g^{-1}\widetilde Yg)=\operatorname{tr}(\operatorname{diag}(d')Y)\quad(Y\in M_n(\mathbb C)),$$ and $d'_a-d'_b\ge1$ whenever $a<b$.

There are $C,t_0\in\mathbb R$ such that for every $t\ge t_0$ for which $\lambda+td$ is a Harish–Chandra parameter and $$|(\lambda+td)_a-(\lambda+td)_b|\ge200(n+1)^3\quad\text{if }\epsilon_a\ne\epsilon_b,$$ every Hilbert representation $\pi$ of $U(\epsilon)$ satisfying the discrete-series conditions of ([Arbitrary complex Lie words on the lowest compact type](https://andrewodesky.com/rh/lean/CompanionTheory.Lime.T3.kFiniteWordBound_indefUnitary/)) at $\lambda+td$ has a Harish–Chandra parameter $\mu\in\mathbb R^n$ satisfying $$|\mu_a-td'_a|\le C\sqrt t\quad(1\le a\le n).$$ For every Hilbert representation $\sigma$ of $U(\epsilon')$ satisfying those conditions at $\mu$, there is a nonzero bounded complex-linear map $J:H_\sigma\to H_\pi$ with $J\sigma(h)=\pi(j(h))J$. In rank $r$, a Harish–Chandra parameter here is a strictly decreasing tuple with every entry in $(r-1)/2+\mathbb Z$.
