# E0-230_Computational_methods_of_optimization
E0: 230:Computational Method of Optimization is a course on mathematical optimization of the computer science department at IISc, Bengaluru

:accessibility: Highlights of crucial optimization algorithms and tactics along with their real-world applications:

## Standard Optimization Problem Template
> Objective function $f:\mathbb{R}^d \to \mathbb{R}$
>
> Constrain: $S\subset \mathbb{R}^d$
>
> Find $x^{\ast}=argmin_{x\subset S}\ f(x)$
> and $f(x^{\ast})$

### Standard iterative algorithm:

> pick $x\in S$
>
> $\textbf{while}\ x$  is not optimal solution $\textbf{do}:$
> 
> Pick another $x\in S$ such that $f(x)$ decreases;
> 
> $\textbf{end}$
>
> return $(x,\ f(x))$

## Part-I: Mathematical foundation of optimization theory

> $\bullet$ Mathematical Analysis: $[\delta - \epsilon]$ definition of Limit
> $\bullet$ Lipshitz Continuity
> 
> $\bullet$ Asymptotic notations: $\mathcal{O}(f(x)),\mathcal{\Omega}(f(x))\ and\ \mathcal{o}(f(x)) $
> $\bullet$ Metric Space: Open and Compact sets

> $\bullet$ Multivariate Calculus and Tylor Series Analysis

> $\bullet$ Weistrass theorem: the existence of minima and maxima of a function
> 
> $\bullet$ Gradient and Hessian of a function: Sufficient condition for the existence of local minima
> 
> $\bullet$ Analysis of special matrices: Positive definite (PD), negative definite(ND) and positive semi-definite (PSD) matrices


## Part-II: Convex Function and its Optimization 

⭐ $\bullet$ Convex function and existence of global minima

> Quadratic form and closed form solution:
>
> $f(x)=x^TQx-d^Tx \implies \nabla f(x) = Qx-d\ and\ H(f(x))=Q$
>
> $\implies x^{\ast} = Q^{-1}d$
>
> Computational complexity: $\mathcal{O}{n^3}$ via Gauss Elimination [Hnece, practically useless for large matrices]

> Descent-based algorithm for approximately searching the minima:
> 
> > Exact line search: Kantarovich inequality
> > 
> > Ineaxct line search: Goldstein and Wolfe condition

## Part-III: Generic algorithms for optimizations
⭐ Coordinate descent algorithm
>
⭐ Conjugate descent algorithm:  
