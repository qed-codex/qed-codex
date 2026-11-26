---
{
  "module": "src/Development/AutomorphicArithmetic/MeanSquareBounds/PairExists.lean",
  "declarations": [
    "QH.pair_exists"
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

## Auxiliary prime pairs with uniform character estimates

[Theorem ANT.0365](https://andrewodesky.com/rh/lean/QH.pair_exists/)

There is $C>0$ such that for every $0<\varepsilon<1/52$, $\tau>0$, $K\ge1$ and integer $N_0\ge1$, the following holds for all sufficiently large real $Y$. Put $z=Y^{\varepsilon/5}$. For every real $X\le Y^K$ and $$z(\log Y)^2\le z'\le K^2z(\log Y)^2,$$ there are primes $N_0<q<d$ satisfying $$q\equiv3\pmod8,\quad d\equiv7\pmod{16},\quad z/2<\log q\le z,\quad z'/2<\log d\le z',$$ and $p\mid d+1$ for every odd prime $p$ with $p\le z$ or $p=q$. For every character $\xi$ modulo $N_0$, the functions $$n\longmapsto\xi(n)\left(\frac nq\right),\qquad n\longmapsto\xi(n)\left(\frac nq\right)^a\left(\frac nd\right)\quad(a=0,1)$$ have the following property. Every primitive character $\psi$ modulo $N\ge1$ agreeing with the first function on integers coprime to $N_0q$, respectively the second on integers coprime to $N_0qd$, is nontrivial, has $$N\le B,\qquad L(s,\psi)\ne0\quad(\Re s>1-1/400,\ |\Im s|\le B),$$ $$\left|\frac{L'(1,\psi)}{L(1,\psi)}\right|\le C\log Y,\qquad |G_\psi(y)|\le y^{1/2+\tau}\quad(Y\le y\le X),$$ where $B=N_0e^z$ for the first function and $B=N_0e^{z+z'}$ for the second.
