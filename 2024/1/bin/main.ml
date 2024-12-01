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

let calc_dist lst1 lst2 =
  let sorted_lst1, sorted_lst2 =
    (List.sort compare lst1, List.sort compare lst2)
  in
  List.fold_left2 (fun diff a b -> diff + abs (a - b)) 0 sorted_lst1 sorted_lst2

let () =
  let lst1, lst2 = get_input "input" in
  let result = calc_dist lst1 lst2 in
  print_int result
