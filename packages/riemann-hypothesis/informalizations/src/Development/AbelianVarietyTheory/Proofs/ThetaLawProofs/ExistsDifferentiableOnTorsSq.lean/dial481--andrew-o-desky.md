---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/ThetaLawProofs/ExistsDifferentiableOnTorsSq.lean",
  "declarations": [
    "GlobalTheory.TorsionHolomorphic.exists_differentiableOn_torsSq"
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

## A local holomorphic choice of squared complex torsion

[Theorem AG.0248](https://andrewodesky.com/rh/lean/GlobalTheory.TorsionHolomorphic.exists_differentiableOn_torsSq/)

Let $E$ be a complex normed vector space, $I$ a finite set, and $d:I\to\mathbb N$ a grading. Let $W\subset E$ be open and $D:E\to M_I(\mathbb C)$ have holomorphic entries on $W$. Assume that for $e\in W$, $$D(e)_{pq}=0\text{ unless }d(q)=d(p)+1,\qquad D(e)^2=0.$$ Define $I_+=\{p:d(p)\text{ is even}\}$ and $I_-=I\setminus I_+$. Say a number $t\in\mathbb C$ satisfies the squared-torsion condition at $e$ if there are a matrix $h\in M_I(\mathbb C)$ and a bijection $\eta:I_+\to I_-$ such that $$h_{pq}=0\text{ unless }d(p)=d(q)+1,\qquad D(e)h+hD(e)=1,$$ $$t=\det\bigl((D(e)+h)_{p,\eta(q)}\bigr)_{p,q\in I_+}^{\,2}.$$ If $e_0\in W$ and $t_0$ satisfies this condition at $e_0$, there are an open neighborhood $W'\subseteq W$ of $e_0$ and a holomorphic function $t:E\to\mathbb C$ on $W'$ satisfying the condition at every $e\in W'$.
