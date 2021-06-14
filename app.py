from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_bs4 import Bootstrap


@app.route('/', methods=['POST', 'GET'])
@app.route('/index', methods=['POST', 'GET'])
def index():
    return render_template('/index.html')

@app.route('/basic_data', methods=['POST', 'GET'])
def basic_data():
    if request.method == "POST":
        students_count = request.form['students_count']
        employee_count = request.form['employee_count']
        staff_count = request.form['staff_count']
        days_count = request.form['days_count']

        basic = Basic_data(students_count=students_count, employee_count=employee_count,
                           staff_count=staff_count, days_count=days_count)

        try:
            db.session.add(basic)
            db.session.commit()
            return redirect('/basic_data')
        except:
            return "Данные внесены не верно"
    else:
        energy = db.session.query(Energy.id).all()
        trash = db.session.query(Trash.id).all()
        water = db.session.query(Water.id).all()
        heat = db.session.query(Heat.id).all()
        basic = Basic_data.query.order_by(Basic_data.id).all()
        return render_template('basic_data.html', heat=heat, basic=basic, energy=energy, trash=trash, water=water)

@app.route('/basic_data/delete/<int:id>')
def delete_basik(id):
    task_to_delete = Basic_data.query.get_or_404(id)
    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/basic_data')
    except:
        return 'There was a problem deleting that task'

@app.route('/energy', methods=['POST', 'GET'])
def energy():
    if request.method == "POST":
        energy_name = request.form['energy_name']
        energy_count = request.form['energy_count']
        energy_power = request.form['energy_power']
        energy_time = request.form['energy_time']
        energy = Energy(energy_name=energy_name,
                        energy_count=energy_count,
                        energy_power=energy_power, energy_time=energy_time)
        try:
            db.session.add(energy)
            db.session.commit()
            return redirect('/energy')
        except:
            return "Данные внесены не верно"
    else:
        basic = db.session.query(Basic_data.id).all()
        trash = db.session.query(Trash.id).all()
        water = db.session.query(Water.id).all()
        heat = db.session.query(Heat.id).all()
        energy = Energy.query.order_by(Energy.id).all()
        return render_template('energy.html', heat=heat, basic=basic,
                               energy=energy, trash=trash, water=water)

@app.route('/energy/delete/<int:id>')
def delete(id):
    task_to_delete = Energy.query.get_or_404(id)

    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/energy')
    except:
        return 'There was a problem deleting that task'

@app.route('/water', methods=['POST', 'GET'])
def water():
    if request.method == "POST":
        water_name = request.form['water_name']
        water_count = request.form['water_count']
        water_hot = request.form['water_hot']
        water_cold = request.form['water_cold']
        water = Water(water_name=water_name,
                      water_count=water_count,
                      water_hot=water_hot, water_cold=water_cold)
        try:
            db.session.add(water)
            db.session.commit()
            return redirect('/water')
        except:
            return "Данные внесены не верно"
    else:
        basic = db.session.query(Basic_data.id).all()
        energy = db.session.query(Energy.id).all()
        trash = db.session.query(Trash.id).all()
        heat = db.session.query(Heat.id).all()
        water = Water.query.order_by(Water.id).all()
        return render_template('water.html', heat=heat, basic=basic,
                               energy=energy, trash=trash, water=water)

@app.route('/water/delete/<int:id>')
def delete_wa(id):
    task_to_delete = Water.query.get_or_404(id)

    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/water')
    except:
        return 'There was a problem deleting that task'

@app.route('/trash', methods=['POST', 'GET'])
def trash():
    if request.method == "POST":
        trash_name = request.form['trash_name']
        trash_count = request.form['trash_count']
        trash_type = request.form['trash_type']
        trash_style = request.form['trash_style']
        trash = Trash(trash_name=trash_name,
                      trash_type=trash_type,
                      trash_count=trash_count, trash_style=trash_style, )
        try:
            db.session.add(trash)
            db.session.commit()
            return redirect('/trash')
        except:
            return "Данные внесены не верно"
    else:
        basic = db.session.query(Basic_data.id).all()
        energy = db.session.query(Energy.id).all()
        water = db.session.query(Water.id).all()
        heat = db.session.query(Heat.id).all()
        trash = Trash.query.order_by(Trash.id).all()
        return render_template('trash.html', heat=heat, basic=basic,
                               energy=energy, trash=trash, water=water)

@app.route('/trash/delete/<int:id>')
def delete_tr(id):
    task_to_delete = Trash.query.get_or_404(id)

    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/trash')
    except:
        return 'There was a problem deleting that task'

@app.route('/teplo', methods=['POST', 'GET'])
def teplo():
    if request.method == "POST":
        heat_name = request.form['heat_name']
        delta_heat = request.form['delta_heat']
        heat_days = request.form['heat_days']
        heat_square = request.form['heat_square']
        heat_power = request.form['heat_power']
        heat = Heat(delta_heat=delta_heat,
                    heat_days=heat_days, heat_name=heat_name,
                    heat_square=heat_square, heat_power=heat_power)
        try:
            db.session.add(heat)
            db.session.commit()
            return redirect('/teplo')
        except:
            return "Данные внесены не верно"
    else:
        basic = db.session.query(Basic_data.id).all()
        energy = db.session.query(Energy.id).all()
        trash = db.session.query(Trash.id).all()
        water = db.session.query(Water.id).all()
        heat = Heat.query.order_by(Heat.id.desc()).all()
        return render_template('teplo.html', heat=heat, basic=basic,
                               energy=energy, trash=trash, water=water)

@app.route('/teplo/delete/<int:id>')
def delete_te(id):
    task_to_delete = Heat.query.get_or_404(id)

    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/teplo')
    except:
        return 'There was a problem deleting that task'

@app.route('/calculate')
def calculate():
    students_count= db.session.query(Basic_data.students_count).all()
    employee_count= db.session.query(Basic_data.employee_count).all()
    staff_count= db.session.query(Basic_data.staff_count).all()
    days_count= db.session.query(Basic_data.days_count).all()

    energy_count= db.session.query(Energy.energy_count).all()
    energy_power= db.session.query(Energy.energy_power).all()
    energy_time= db.session.query(Energy.energy_time).all()

    water_count = db.session.query(Water.water_count).all()
    water_hot = db.session.query(Water.water_hot).all()
    water_cold = db.session.query(Water.water_cold).all()

    trash_count = db.session.query(Trash.trash_count).all()
    trash_type = db.session.query(Trash.trash_type).all()
    trash_style = db.session.query(Trash.trash_style).all()

    heat_delta = db.session.query(Heat.delta_heat).all()
    heat_days = db.session.query(Heat.heat_days).all()
    heat_square = db.session.query(Heat.heat_square).all()
    heat_power = db.session.query(Heat.heat_power).all()

    people_count = 0
    for i in range(len(students_count)):
        people_count += students_count[i][0]+employee_count[i][0]+staff_count[i][0]

    energy_calc = 0.0
    for i in range(len(energy_count)):
        energy_calc += float(energy_count[i][0])*energy_power[i][0]*energy_time[i][0]
    energy_calc = float("{0:.3f}".format(energy_calc/1000*float(days_count[0][0])/24))
    water_calc = 0.0
    for i in range(len(water_count)):
        water_calc += float(water_count[i][0])*(water_hot[i][0]+water_cold[i][0])
    water_calc = float("{0:.3f}".format(water_calc/1000))
    trash_calc = 0.0
    for i in range(len(trash_count)):
        if str.lower(trash_type[i][0])=="пластмасса" and str.lower(trash_style[i][0]) == "да":
            trash_calc += trash_count[i][0]*0.9
        elif str.lower(trash_type[i][0])=="стекло" and str.lower(trash_style[i][0]) == "да":
            trash_calc += trash_count[i][0]*0.95
        elif str.lower(trash_type[i][0])=="бумага" and str.lower(trash_style[i][0]) == "да":
            trash_calc += trash_count[i][0] * 0.75
        else:
            trash_calc += trash_count[i][0]
    trash_calc = float("{0:.3f}".format(trash_calc/1000/days_count[0][0]))

    teplo_calc = 0.0
    grade_teplo = 0.0
    for i in range(len(heat_days)):
        teplo_calc += heat_power[i][0]*0.00086
        grade_teplo += (heat_square[i][0]*3.3*1.4*(21-heat_delta[i][0]))/1000000

    print(heat_power[i][0])

    grade_energy = float("{0:.3f}".format(200*people_count))
    grade_energy_people= 200
    grade_water=float("{0:.3f}".format(277/1000*people_count))
    grade_water_people=277/1000
    grade_trash = round(((students_count[0][0]*22+(employee_count[0][0]+staff_count[0][0])*156))/1000/days_count[0][0])
    grade_trash_people =float("{0:.3f}".format((students_count[0][0]*22+(employee_count[0][0]+staff_count[0][0])*156)/people_count))

    teplo_calc = float("{0:.3f}".format(teplo_calc))
    grade_teplo = float("{0:.3f}".format(grade_teplo))
    grade_teplo_people =float("{0:.3f}".format(grade_teplo/people_count))

    return render_template('calculate.html', water_calc=water_calc,
                           energy_calc=energy_calc, trash_calc=trash_calc,
                           grade_trash=grade_trash, teplo_calc=teplo_calc,
                           grade_teplo=grade_teplo, people_count=people_count,
                           grade_energy=grade_energy, grade_energy_people=grade_energy_people,
                           grade_water=grade_water, grade_water_people=grade_water_people,
                           grade_trash_people=grade_trash_people, grade_teplo_people=grade_teplo_people)



if __name__ == "__main__":
    app.run(port=3200, debug=True)
