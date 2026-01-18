

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# --- YOUR SUDOKU LOGIC (Adapted) ---

def valid(s, g, p):
    # Check Row
    for i in range(len(s[0])):
        if s[p[0]][i] == g and p[1] != i:
            return False
    
    # Check Column
    for i in range(len(s)):
        if s[i][p[1]] == g and p[0] != i:
            return False
            
    # Check 3x3 Box
    bx = p[1] // 3
    by = p[0] // 3
    for i in range(by * 3, by * 3 + 3):
        for j in range(bx * 3, bx * 3 + 3):
            if s[i][j] == g and (i, j) != p:
                return False
    return True

def empty(s):
    for i in range(len(s)):
        for j in range(len(s[0])):
            if s[i][j] == 0:
                return (i, j)
    return None

def solve_logic(s):
    """
    Renamed to solve_logic to avoid conflict with route name.
    Returns True if solved, False otherwise.
    """
    f = empty(s)
    if not f:
        return True
    else:
        r, c = f

    for i in range(1, 10):
        if valid(s, i, (r, c)):
            s[r][c] = i
            if solve_logic(s):
                return True
            s[r][c] = 0
            
    return False

# --- FLASK ROUTES ---

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/solve', methods=['POST'])
def solve_sudoku():
    try:
        data = request.get_json()
        grid = data['grid']
        
        # Convert empty strings to 0 for the solver
        # and ensure numbers are integers
        processed_grid = []
        for row in grid:
            new_row = []
            for cell in row:
                if cell == "" or cell is None:
                    new_row.append(0)
                else:
                    new_row.append(int(cell))
            processed_grid.append(new_row)

        # Run the solver
        if solve_logic(processed_grid):
            return jsonify({'status': 'success', 'solution': processed_grid})
        else:
            return jsonify({'status': 'error', 'message': 'No solution exists for this board.'})
            
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

if __name__ == '__main__':
    app.run(debug=True)