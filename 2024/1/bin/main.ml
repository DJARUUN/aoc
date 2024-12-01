open Containers

let create_lsts str =
  let rec aux lst1 lst2 = function
    | "" -> (lst1, lst2)
    | str' ->
        let id1, str' = String.take_drop 5 str' in
        let id2, str' = str' |> String.drop 3 |> String.take_drop 5 in
        let str' = String.drop 1 str' in
        aux (id1 :: lst1) (id2 :: lst2) str'
  in
  aux [] [] str

let get_input filename =
  let contents = In_channel.with_open_text filename In_channel.input_all in
  let lst1, lst2 = create_lsts contents in
  (List.map Int.of_string_exn lst1, List.map Int.of_string_exn lst2)

let calc_similarity lst1 lst2 =
  List.fold_left
    (fun similarity a ->
      let times_in_lst2 = List.count (fun b -> a = b) lst2 in
      similarity + (a * times_in_lst2))
    0 lst1

let () =
  let lst1, lst2 = get_input "input" in
  let result = calc_similarity lst1 lst2 in
  print_int result
