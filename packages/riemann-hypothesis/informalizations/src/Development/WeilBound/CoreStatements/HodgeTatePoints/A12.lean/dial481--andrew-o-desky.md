---
{
  "module": "src/Development/WeilBound/CoreStatements/HodgeTatePoints/A12.lean",
  "declarations": [
    "PositivityTheory.HtPt.Ktw.a12",
    "PositivityTheory.HtPt.Ktw.a13",
    "PositivityTheory.HtPt.Ktw.a17"
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

## A Hilbert polynomial for localized multigraded sections

[Theorem AG.0067](https://andrewodesky.com/rh/lean/PositivityTheory.HtPt.Ktw.a17/)

Let $F\subseteq\Omega$ be fields, $K$ a finite set with a distinguished element $k_0$, and $I_k$ finite coordinate sets. Choose $y_{k,i}\in\Omega$ with a nonzero coordinate in each block. For each choice $c=(c_k)$ with $y_{k,c_k}\ne0$ put $$A_c=F[y_{k,i}/y_{k,c_k}:k\in K,\ i\in I_k]\subseteq\Omega.$$ Suppose that the collection of subrings $(A_c)_{\mathfrak p}\subset\Omega$, as $c$ varies and $\mathfrak p$ ranges over prime ideals of $A_c$, is exactly the collection of local rings obtained from the single block $(y_{k_0,i})_{i\in I_{k_0}}$ by the same construction. Let $J$ be the kernel of $F[z_{k,i}]\to\Omega[t_k:k\in K]$, $z_{k,i}\mapsto y_{k,i}t_k$. For $\alpha\in\mathbb Z^K$ let $h_J(\alpha)$ be the dimension of the multidegree-$\alpha$ component of $F[z]/J$ and put $$S(\alpha)=\{s\in\Omega:s\prod_ky_{k,c_k}^{-\alpha_k}\in A_c\text{ for every permitted }c\}.$$ There is $P\in\mathbb Q[T_k:k\in K]$ such that $h_J(\alpha)=P(\alpha)$ whenever all coordinates of $\alpha$ are sufficiently large, and, for every $\beta\in\mathbb Z^K$ and all sufficiently large integers $c\ge0$, $$\dim_FS(\beta+ce_{k_0})=P(\beta+ce_{k_0}),$$ where $e_{k_0}$ is the coordinate unit vector.

## A polynomial Euler characteristic in every multidegree

[Theorem AG.0338](https://andrewodesky.com/rh/lean/PositivityTheory.HtPt.Ktw.a12/)

Let $F$ be a field, $K$ a finite linearly ordered set, and $(I_k)_{k\in K}$ finite linearly ordered sets. Give $R=F[X_{ki}:k\in K,i\in I_k]$ its block multigrading, and let $J\subseteq R$ be a multihomogeneous ideal. There are $B\ge0$ and $\chi\in\mathbb Q[T_k:k\in K]$ such that the standard multigraded Čech cohomology groups $H^i(\mathbf m)$ of $R/J$ are finite-dimensional over $F$ for all $\mathbf m\in\mathbb Z^K$ and $i\ge0$, vanish for $i>B$, and satisfy $$\sum_{i=0}^{B}(-1)^i\dim_FH^i(\mathbf m)=\chi(\mathbf m)\qquad(\mathbf m\in\mathbb Z^K).$$

## Serre vanishing in sufficiently large multidegrees

[Theorem AG.0391](https://andrewodesky.com/rh/lean/PositivityTheory.HtPt.Ktw.a13/)

Let $F$ be a field, $K$ a finite ordered set, and $I_k$ finite ordered coordinate sets. Let $V\subseteq F[x_{k,i}:k\in K,\ i\in I_k]$ be an ideal homogeneous for the grading $\deg x_{k,i}=e_k\in\mathbb Z^K$. For every sufficiently large multidegree $m$ componentwise, $$\check H^i(m)=0\quad(i\ge1),\qquad \dim_F\check H^0(m)=h_V(m).$$
