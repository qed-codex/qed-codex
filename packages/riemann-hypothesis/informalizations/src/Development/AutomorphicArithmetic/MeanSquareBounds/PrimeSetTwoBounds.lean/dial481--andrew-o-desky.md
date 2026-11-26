---
{
  "module": "src/Development/AutomorphicArithmetic/MeanSquareBounds/PrimeSetTwoBounds.lean",
  "declarations": [
    "QH.Box",
    "QH.BoxAll",
    "QH.GoodC",
    "QH.GoodD",
    "QH.GoodQ",
    "QH.Ind",
    "QH.MeanSq",
    "QH.admitted",
    "QH.primePairSetFirst",
    "QH.primeSetTwoBounds"
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

## Logarithmic derivative from a fixed zero-free rectangle

[Theorem ANT.0166](https://andrewodesky.com/rh/lean/QH.kappa4/)

Fix $0<\varepsilon<1/52$ and a real constant $B>0$. There is $U_0\ge1$ such that for every real $U\ge U_0$, every real $Q$, every integer $N\ge1$ and every nonprincipal complex Dirichlet character $\chi$ modulo $N$, the following implication holds. If $$U^{\varepsilon/6}\le\log Q\le B U^{\varepsilon/5}(\log U)^2,\qquad N\le Q,$$ and $$L(s,\chi)\ne0\qquad(\Re s>399/400,\ |\Im s|\le Q),$$ then $$\left|\frac{L'}{L}(1,\chi)\right|\le4\log U.$$ The threshold $U_0$ depends only on $\varepsilon$ and $B$; primitivity is not assumed.

## Extending the identity for a primitive quadratic twist

[Theorem ANT.0167](https://andrewodesky.com/rh/lean/QH.ind_drop/)

Let $B,H,N\ge1$ be integers, let $q$ be an odd prime with $q\nmid B$, let $\xi$ be a complex Dirichlet character modulo $B$, and let $\chi$ be a primitive complex Dirichlet character modulo $N$. Suppose $$\chi(n)=\xi(n)\left(\frac nq\right)\qquad\text{for every }n\in\mathbb N\text{ with }(n,H)=1,$$ where the parenthesized symbol is the Jacobi symbol. Then $$\chi(n)=\xi(n)\left(\frac nq\right)\qquad\text{for every }n\in\mathbb N\text{ with }(n,Bq)=1.$$

## Mean square over auxiliary quadratic twists

[Theorem ANT.0055](https://andrewodesky.com/rh/s/twist-mean-square.html)

There is an absolute $C>0$ with the following property. Fix $0<\varepsilon\le1$ and $A\ge1$. For all sufficiently large $Y$, let $m>0$, $8\mid m$, $(a,m)=1$, and $U>0$ satisfy $$\tfrac14(\log Y)^2\log m\le\log U,\qquad Y^{\varepsilon/6}\le\log U\le Y^{\varepsilon/5}(\log Y)^2.$$ Assume every prime divisor $p$ of $m$ satisfies either $p\le Y^{\varepsilon/5}$ or $p>(Y^A)^{400}$. Set $Z=(Y^A)^{400}$ and $P=\{q\text{ prime}:\sqrt U<q\le U,\ q\equiv a\pmod m\}$. For $Y\le y\le Y^A$ and any $\kappa:\mathbb N\to\mathbb C$ with $|\kappa(n)|\le1$, $$\sum_{q\in P}\left|\sum_{1\le n\le Z}\Lambda(n)\min(1,y/n)\kappa(n)\left(\frac n q\right)\right|^2\le C y\log y\,|P|.$$ Here $\Lambda$ is the von Mangoldt function and the parenthesized symbol is the Jacobi symbol.

## Good auxiliary primes and good pairs: uniform estimates for the twisted characters

[Definition / hypothesis ANT.D274](https://andrewodesky.com/rh/lean/QH.GoodQ/)

Let $N_0\ge1$ be an integer and let $C,\tau,Y,X,z,z'$ be real numbers with $Y\ge1$. For a primitive Dirichlet character $\chi$, let $L(s,\chi)$ and $g_\chi$ be the functions of ([Regularized smoothed character sums](https://andrewodesky.com/rh/lean/Deduction.Gchi/)).

**The estimates.** Let $B$ be a real number. A primitive Dirichlet character $\chi$ of conductor $N$ *satisfies the estimates with bound $B$* when $\chi$ is nonprincipal, $N\le B$, $$L(s,\chi)\ne0\quad\text{for every }s\in\mathbb C\text{ with }\Re s>\tfrac{399}{400}\text{ and }|\Im s|\le B,$$ $$\left|\frac{L'(1,\chi)}{L(1,\chi)}\right|\le C\log Y\qquad\text{and}\qquad|g_\chi(y)|\le y^{1/2+\tau}\quad\text{for every }y\in[Y,X].$$

**Good primes and good pairs.** Let $q$ and $d$ be odd primes. The prime $q$ is *good* for $N_0,C,\tau,Y,X,z$ when, for every Dirichlet character $\xi$ modulo $N_0$, every primitive Dirichlet character $\chi$ with $$\chi(n)=\xi(n)\left(\frac nq\right)\qquad\text{for all integers }n\ge1\text{ coprime to }N_0q$$ satisfies the estimates with bound $N_0e^{z}$. The pair $(q,d)$ is *good* for $N_0,C,\tau,Y,X,z,z'$ when, for every Dirichlet character $\xi$ modulo $N_0$ and every $a\in\{0,1\}$, every primitive Dirichlet character $\chi$ with $$\chi(n)=\xi(n)\left(\frac nq\right)^{a}\left(\frac nd\right)\qquad\text{for all integers }n\ge1\text{ coprime to }N_0qd$$ satisfies the estimates with bound $N_0e^{z+z'}$.

**The sets of primes.** Let $\mathcal Q(z)$ be the set of primes $q$ with $$q\equiv3\pmod8,\qquad e^{z/2}<q\le e^{z}.$$ For a prime $q$, let $\mathcal D(z,z',q)$ be the set of primes $d$ with $$d\equiv7\pmod{16},\qquad e^{z'/2}<d\le e^{z'},\qquad q\prod_{\substack{p\text{ prime}\\3\le p\le z}}p\ \Bigm|\ d+1.$$
