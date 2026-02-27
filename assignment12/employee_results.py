import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

def main():
    # Connect to ../db/lesson.db
    conn = sqlite3.connect("../db/lesson.db")

    sql = """
    SELECT last_name, SUM(price * quantity) AS revenue
    FROM employees e
    JOIN orders o ON e.employee_id = o.employee_id
    JOIN line_items l ON o.order_id = l.order_id
    JOIN products p ON l.product_id = p.product_id
    GROUP BY e.employee_id;
    """

    # Loading SQL results into a DataFrame
    employee_results = pd.read_sql_query(sql, conn)

    conn.close()

    # Bar chart using Pandas plotting
    ax = employee_results.plot(
        x="last_name",
        y="revenue",
        kind="bar",
        title="Revenue by Employee",
        legend=False,
        color="skyblue"
    )

    # labels
    ax.set_xlabel("Employee Last Name")
    ax.set_ylabel("Revenue")

    # readable x labels
    plt.xticks(rotation=45, ha="right")

    # plot
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
