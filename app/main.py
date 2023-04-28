def copy_file(command: str) -> None:
    args = command.split()
    if len(command.split()) != 3:
        raise ValueError("command should have 3 arguments")
    src_file_path = args[1]
    dst_file_path = args[2]
    if src_file_path == dst_file_path:
        raise
    with (

            open(src_file_path, "r") as file_in,
            open(dst_file_path, "w") as file_out

    ):
        file_out.write(file_in.read())
