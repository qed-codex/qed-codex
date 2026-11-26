---
{
  "module": "src/Formalism/GradedWeylDivisibility/StatementC.lean",
  "declarations": [
    "Formalism.GradedWeylDivisibility.PeelDecomp",
    "Formalism.GradedWeylDivisibility.PeelDegBound",
    "Formalism.GradedWeylDivisibility.PeelHomog",
    "Formalism.GradedWeylDivisibility.PeelLead"
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

## Column slices and substitution bounds for polynomials

[Definition / hypothesis ALG.D067](https://andrewodesky.com/rh/lean/Formalism.GradedWeylDivisibility.PeelDecomp/)

Let $A$ be a commutative ring and let $r,n\ge0$ be integers. Work in $A[X_{bc}:0\le b<r,\ 0\le c<n]$. List variables by increasing column and then increasing row. Compare exponent arrays lexicographically in this order: at the first differing entry, the larger exponent gives the larger monomial. Write $m(g)$ for the largest exponent array occurring with nonzero coefficient in $g$, and set $m(0)=0$.

For distinct columns $l,j$, let $D_{lj}g$ be the polynomial in $A[X_{bc},t]$ obtained by replacing $X_{bj}$ with $X_{bj}+tX_{bl}$ for every row $b$ and fixing the other variables. Write $\deg_t$ for the largest exponent of $t$ occurring with nonzero coefficient, with $\deg_t0=0$.

Let $\mathbf e_{bc}$ be the nonnegative integer array with a single $1$ at $(b,c)$. Give $X_{bj}$ weight $\mathbf e_{bl}$ and every variable outside column $j$ weight $\mathbf e_{bc}$. A polynomial is homogeneous of weight $\omega\in\mathbb N^{r\times n}$ if every monomial with nonzero coefficient has weight $\omega$, where a monomial's weight is the sum of its variable weights counted with their exponents.

For a row $a$ and $k\ge0$, define $P_{a,k}(g)$ by retaining the terms of $g$ whose exponent on $X_{al}$ is $k$, then setting the exponents on $X_{al}$ and $X_{aj}$ to zero in each retained term. Add the coefficients of terms that become equal. All integer parameters below are nonnegative, and subtraction of nonnegative integers is truncated at zero.

The four universal conditions are as follows. Each quantifies over all indicated rings, sizes, columns, rows and polynomials.

1. For every commutative ring $A$, distinct columns $l,j$, row $a$ and polynomial $g$ homogeneous of weight $\omega$, put $q=\omega_{al}$. Then $$g=\sum_{k=0}^{q}X_{al}^kX_{aj}^{q-k}P_{a,k}(g).$$
2. For the same choices and every $k\ge0$, the polynomial $P_{a,k}(g)$ is homogeneous of weight obtained from $\omega$ by setting its $(a,l)$ entry to zero. Every monomial occurring in $P_{a,k}(g)$ has exponent zero on both $X_{al}$ and $X_{aj}$.
3. For every commutative domain $A$, columns $l<j$, row $a$, polynomial $g$ homogeneous of weight $\omega$ and integer $K\ge0$, suppose $\omega_{bl}=0$ for every $b<a$, $P_{a,K}(g)\ne0$, and $P_{a,k}(g)=0$ for every $k>K$. Then $$m(g)=K\mathbf e_{al}+(\omega_{al}-K)\mathbf e_{aj}+m(P_{a,K}(g)).$$
4. For every commutative domain $A$, distinct columns $l,j$, row $a$, integers $K,e,s\ge0$ and family $(w_k)_{k\ge0}$ of polynomials in $A[X_{bc}]$, suppose every monomial of every $w_k$ has exponent zero on $X_{al},X_{aj}$ and $w_K\ne0$. If $$\deg_tD_{lj}\left(\sum_{k=0}^{K}X_{al}^kX_{aj}^{e+(K-k)}w_k\right)\le s,$$ then $$e\le s,\qquad\deg_tD_{lj}w_K\le s-e+K.$$
