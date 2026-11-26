---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/FlagMeasures/ProjAbsHolds.lean",
  "declarations": [
    "GlobalTheory.Dec.projAbs_holds"
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

## The projection defined by a square-integrable matrix coefficient

[Theorem REP.0389](https://andrewodesky.com/rh/lean/GlobalTheory.Dec.projAbs_holds/)

Let $G$ be a second-countable topological group with its Borel measurable structure and a bi-invariant Haar measure $\mu$. Let $\sigma$ be a strongly continuous unitary representation on a complex Hilbert space $H$. Suppose $d>0$ and, for every $x,y\in H$, the squared matrix coefficient is integrable and $$\int_G|\langle y,\sigma(g)x\rangle|^2\,d\mu(g)=\|x\|^2\|y\|^2/d.$$ Let $w\in H$ have norm one and assume $g\mapsto\langle w,\sigma(g)w\rangle$ is integrable. Put $e(g)=d\overline{\langle w,\sigma(g)w\rangle}$. Then $$\overline{e(g^{-1})}=e(g),\qquad\int_Ge(g)e(x^{-1}g^{-1}y)\,d\mu(g)=\langle w,\sigma(x)w\rangle e(y).$$ For every strongly continuous unitary representation $\pi$ on a complex Hilbert space $H'$, there is a bounded operator $P$ satisfying $$\langle u,Pv\rangle=\int_Ge(g)\langle u,\pi(g)v\rangle\,d\mu(g)\qquad(u,v\in H').$$ Every such $P$ is an orthogonal projection and $$P\pi(x)P=\langle w,\sigma(x)w\rangle P\qquad(x\in G).$$ Each unit vector $v$ in its range satisfies $\langle v,\pi(g)v\rangle=\langle w,\sigma(g)w\rangle$ for all $g$, and there is a complex-linear isometric intertwiner $j:H\to H'$ with $j(w)=v$. Moreover, $$\operatorname{ran}P=\{j(w):j:H\to H'\text{ is a bounded complex-linear intertwiner}\}.$$
