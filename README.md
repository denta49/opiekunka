# Customer Loyalty Points System for Opeikunka.eu

A simple command-line application to manage customer loyalty points.  
Implemented in **Python 3.11**, using in-memory storage (data persists only during process runtime).

## Features
- Create new customers with an initial balance
- Earn points for existing customers
- Redeem points with validation rules
- Low balance warning (< 10 points)
- Interactive REPL mode (state persists across multiple commands in one session)

## Requirements

Python 3.11+
## Installation
Clone the repository and enter the project directory:

```bash
git clone <your-repo-url>
cd <your-repo-name>
```

The project uses only Python standard library — no extra dependencies required.

## Usage
One-off commands
Run with python -m loyalty followed by a command:

### Create a new customer with 100 points
```bash
python -m loyalty create user123 100
```

### Add points
```bash
python -m loyalty earn user123 50
```

### Redeem points
```bash
python -m loyalty redeem user123 30
```
### If redeeming leaves a balance below 10, a warning is printed:
`Warning: Customer user123 has a low balance: 5 points.`


## Interactive mode (REPL)

Run without arguments to start an interactive shell:

```bash
python -m loyalty
```

## Commands

```bash
create <customerId> <points> # → create new customer with initial balance
```
```bash
earn <customerId> <points> # → add points to existing customer
```
```bash
redeem <customerId> <points> # → redeem points (fails if insufficient balance)
```

```bash
quit # → exit REPL
exit # → exit REPL
```

## Notes

This implementation uses an in-memory dictionary.

Data is not persisted between runs — state lives only during a single process execution.
