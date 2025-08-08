from task_model import TaskModel

def main():
    task = TaskModel("Estudiar para el examen")
    print(f"Tarea creada: {task.get_task_name()}")
    print(f"¿Está completada? {task.is_task_completed()}")

    task.mark_as_complete()
    print("Tarea marcada como completada.")

    print(f"¿Está completada ahora? {task.is_task_completed()}")

if __name__ == "__main__":
    main()

